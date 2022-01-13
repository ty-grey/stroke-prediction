const submitButton = document.querySelector("#patientFormSubmit");
const patientGender = document.querySelector("#patientGender");
const patientAge = document.querySelector("#patientAge");
const patientHypertension = document.querySelector("#patientHypertension");
const patientHeartDisease = document.querySelector("#patientHeartDisease");
const patientMarry = document.querySelector("#patientMarry");
const patientWork = document.querySelector("#patientWork");
const patientResidence = document.querySelector("#patientResidence");
const patientGlucose = document.querySelector("#patientGlucose");
const patientBmi = document.querySelector("#patientBmi");
const patientSmoking = document.querySelector("#patientSmoking");
const modalCustom = document.querySelector("#modalCustom");
const modalContent1 = document.querySelector("#modalContent1");
const modalContent2 = document.querySelector("#modalContent2");
const modalContent3 = document.querySelector("#modalContent3");
const modalButton = document.querySelector("#modalButton");
const modalTitle = document.querySelector("#modalTitle");

function formCollection() {
    if (!patientAge.value || !patientGlucose.value || !patientBmi.value) {
        showErrorModal("Missing Values in the Form",
            "Please ensure all entries in the form are filled!");
    } else if (patientAge.value < 0 || patientGlucose.value < 0 || patientBmi.value < 0) {
        showErrorModal("Incorrect Values in the Form",
            "Please ensure all entries in the form are filled with non-negative and valid values!");
    } else {
        // Arrange data for sending to api
        var information = [
            [parseInt(patientGender.value), parseInt(patientAge.value),
                patientHypertension.checked ? 1 : 0,
                patientHeartDisease.checked ? 1 : 0,
                patientMarry.checked ? 1 : 0,
                parseInt(patientWork.value), parseInt(patientResidence.value),
                parseInt(patientGlucose.value), parseInt(patientBmi.value),
                parseInt(patientSmoking.value)
            ]
        ];

        data = {
            information: information
        };

        fetch('/probability/', {
            method: 'POST',
            body: JSON.stringify(data),
            headers: {
                'Content-type': 'application/json; charset=UTF-8'
            }
        }).then(function(response) {
            if (response.ok) {
                return response.json();
            }
            return Promise.reject(response);
        }).then(function(data) {
            showSuccessModal(data);
        }).catch(function(error) {
            console.warn('Error: ', error);
            showErrorModal("Error retrieving stroke probability information",
                "There has been an error retrieving the information.  Please try again in 5-10 minutes.");
        });
    }
}

function showModal() {
    modalCustom.style.display = "block";
    modalCustom.style.paddingRight = "17px";
    modalCustom.className = "modal fade show";
}

function showSuccessModal(data) {
    modalTitle.innerHTML = "Patient Stroke Probability Information";
    var accuracy = data.accuracy;
    var probability = data.probability[0];
    var noStroke = probability[0];
    var strokeMessage = "";

    if (noStroke > .8) {
        strokeMessage = "Incredibly Unlikely";
    } else if (noStroke > .6) {
        strokeMessage = "Unlikely";
    } else if (noStroke > .45) {
        strokeMessage = "Average Chance";
    } else if (noStroke > .25) {
        strokeMessage = "Moderate Chance";
    } else {
        strokeMessage = "High Likelihood";
    }

    modalContent1.innerHTML = "Chance of patient having a stroke in the future: " + strokeMessage;
    modalContent2.innerHTML = "Chance of not having a stroke in the future: " + probabilityToPercentage(probability[0]) +
        "<br><br>Chance of having a stroke: " + probabilityToPercentage(probability[1]);
    modalContent3.innerHTML = "Accuracy of model: " + probabilityToPercentage(accuracy);
    showModal();
}

function showErrorModal(content1, content2) {
    modalTitle.innerHTML = "Error";
    modalContent1.innerHTML = content1;
    modalContent2.innerHTML = content2;
    showModal();
}

function probabilityToPercentage(probability) {
    return String(parseFloat(probability).toFixed(6) * 100 + "%");
}

// Hide the modal
modalButton.addEventListener('click', (e) => {
    modalCustom.style.display = "none";
    modalCustom.className = "modal fade";
});