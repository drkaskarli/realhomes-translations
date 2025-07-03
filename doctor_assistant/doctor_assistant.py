import json
import os
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.json')


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {'patients': {}, 'appointments': []}


def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)


def add_patient(patient_id, name, age):
    data = load_data()
    data['patients'][patient_id] = {'name': name, 'age': age}
    save_data(data)
    print(f"Patient {name} added with ID {patient_id}.")


def list_patients():
    data = load_data()
    for pid, info in data['patients'].items():
        print(f"ID: {pid}, Name: {info['name']}, Age: {info['age']}")


def add_appointment(patient_id, date_str, description):
    data = load_data()
    if patient_id not in data['patients']:
        print(f"Patient ID {patient_id} not found.")
        return
    appointment = {
        'patient_id': patient_id,
        'date': date_str,
        'description': description
    }
    data['appointments'].append(appointment)
    save_data(data)
    print(f"Appointment for patient {patient_id} added on {date_str}.")


def list_appointments():
    data = load_data()
    for appt in data['appointments']:
        patient = data['patients'].get(appt['patient_id'], {'name': 'Unknown'})
        print(f"Date: {appt['date']} - Patient: {patient['name']} - Description: {appt['description']}")


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Simple Doctor Assistant (Not for medical advice)')
    subparsers = parser.add_subparsers(dest='command')

    add_p = subparsers.add_parser('add-patient', help='Add a new patient')
    add_p.add_argument('id')
    add_p.add_argument('name')
    add_p.add_argument('age', type=int)

    list_p = subparsers.add_parser('list-patients', help='List all patients')

    add_a = subparsers.add_parser('add-appointment', help='Add appointment for a patient')
    add_a.add_argument('patient_id')
    add_a.add_argument('date')
    add_a.add_argument('description')

    list_a = subparsers.add_parser('list-appointments', help='List all appointments')

    args = parser.parse_args()

    if args.command == 'add-patient':
        add_patient(args.id, args.name, args.age)
    elif args.command == 'list-patients':
        list_patients()
    elif args.command == 'add-appointment':
        add_appointment(args.patient_id, args.date, args.description)
    elif args.command == 'list-appointments':
        list_appointments()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
