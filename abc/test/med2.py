import csv
from datetime import datetime

# med_input.txt faylını oxumaq
with open('med_input.txt', 'r') as med_input_file:
    med_input_lines = med_input_file.readlines()

# Nəticəni yazmaq üçün med_output.txt faylı formatında məlumatları saxlamaq
output = []
for line in med_input_lines:
    data = line.split('|')
    if data[8].strip().lower() == "active":  # "Active" olanları seçmək
        patient_id = data[1]
        medication_name = data[65]
        start_date = data[5].split()[0].replace('-', '')  # YYYYMMDD formatı
        end_date = data[6].split()[0].replace('-', '') if data[6].strip() else ""
        ndc_code = data[63]
        dose = data[68]
        instructions = data[81]

        # HL7 MSH bölməsi
        msh = f"MSH|^~\\&|TouchWorks|Southwest Medical Associates|Rhapsody^Rhapsody|Epic^Epic|{datetime.now().strftime('%Y%m%d%H%M%S')}||RDE^O11|{patient_id}_TW{ndc_code}|P|2.5.1"
        
        # HL7 PID bölməsi
        pid = f"PID|||{patient_id}^^^^TWSMAMRN||{data[93]}^{data[94]}||{data[96].replace('-', '')}|{data[97]}|||{data[99]}^^{data[101]}^{data[102]}^{data[103]}||{data[107]}^^^{data[109]}"

        # HL7 ORC bölməsi
        orc = f"ORC|NW||SMATW-{ndc_code}-{patient_id}||||^^^^^{dose}||{start_date}|||"

        # HL7 RXE bölməsi
        rxe = f"RXE|^^^^^{dose}|{ndc_code}^{medication_name}^NDC|||||^{instructions}||G|||0|||SMATW-{ndc_code}-{patient_id}|||||||||||||||||{start_date}"

        # HL7 RXR bölməsi
        rxr = "RXR|OR^Oral"

        # Məlumatları yığmaq
        output.append("\n".join([msh, pid, orc, rxe, rxr]))

# med_output.txt faylını yazmaq
with open('med_output.txt', 'w') as med_output_file:
    med_output_file.write("\n\n".join(output))

print("med_output.txt yaradıldı!")