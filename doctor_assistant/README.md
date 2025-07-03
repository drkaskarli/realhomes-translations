# Doctor Assistant

This is a simple command-line tool to help manage basic office tasks such as storing patient records and scheduling appointments.

**Disclaimer:** This code is not intended for diagnosing or treating any medical condition. It only provides a basic way to store and view information. Always consult a qualified medical professional for medical advice.

## Usage

```bash
python doctor_assistant.py add-patient PATIENT_ID NAME AGE
python doctor_assistant.py list-patients
python doctor_assistant.py add-appointment PATIENT_ID DATE DESCRIPTION
python doctor_assistant.py list-appointments
```

Appointments and patient data are stored locally in a `data.json` file within this folder.
