def main_message(input_message, output_rdeo11):
    sDx = ""
    sEndDttm = ""
    sNonActiveDTTM = ""
    sPriority = ""
    sStartDttm = ""
    sTW_MRN_OrdID = ""

    for i in range(len(input_message.MED)):
        sTW_MRN_OrdID = f"{input_message.MED[i].APM_MRN}_{input_message.MED[i].OrderNumberEXT}"

        # MSH segment
        output_rdeo11.MSH.SendingApplication.NamespaceID = mshDefault_SendingApp_TW
        output_rdeo11.MSH.SendingFacility.NamespaceID = defaultSendingFac
        output_rdeo11.MSH.ReceivingApplication.NamespaceID = mshDefault_ReceivingApp
        output_rdeo11.MSH.ReceivingApplication.UniversalID = mshDefault_ReceivingApp
        output_rdeo11.MSH.ReceivingFacility.NamespaceID = mshDefault_ReceivingFac
        output_rdeo11.MSH.ReceivingFacility.UniversalID = mshDefault_ReceivingFac

        set_encoded_value(output_rdeo11.MSH.DateTimeOfMessage, date_change_format(current_date_time(True), "MM/dd/yyyy HH:mm:ss", "HL7"))

        output_rdeo11.MSH.MessageType.MessageCode = "RDE"
        output_rdeo11.MSH.MessageType.TriggerEvent = "O11"
        output_rdeo11.MSH.MessageControlID = sTW_MRN_OrdID
        output_rdeo11.MSH.ProcessingID.ProcessingID = mshDefault_ProcessingID
        output_rdeo11.MSH.VersionID.VersionID = mshDefault_VersionID

        # PID segment
        output_rdeo11.PID.PatientIdentifierList[0].IDNumber = input_message.MED[i].APM_MRN
        output_rdeo11.PID.PatientIdentifierList[0].IdentifierTypeCode = defaultMRNID
        output_rdeo11.PID.PatientName[0].FamilyName.Surname = input_message.MED[i].APM_Patient_Last_Name
        output_rdeo11.PID.PatientName[0].GivenName = input_message.MED[i].APM_Patient_First_Name
        output_rdeo11.PID.PatientName[0].MiddleInitialOrName = input_message.MED[i].APM_Patient_MI

        set_encoded_value(output_rdeo11.PID.DateTimeOfBirth, date_change_format(str_left(input_message.MED[i].APM_Patient_DOB, 10), "yyyy-MM-dd", "yyyyMMdd"))

        output_rdeo11.PID.AdministrativeSex = input_message.MED[i].APM_Patient_Sex
        output_rdeo11.PID.PatientAddress[0].StreetAddress.StreetOrMailingAddress = input_message.MED[i].APM_Patient_Street1
        output_rdeo11.PID.PatientAddress[0].OtherDesignation = input_message.MED[i].APM_Patient_Street2
        output_rdeo11.PID.PatientAddress[0].City = input_message.MED[i].APM_Patient_City
        output_rdeo11.PID.PatientAddress[0].StateOrProvince = str_trim(input_message.MED[i].APM_Patient_State)
        output_rdeo11.PID.PatientAddress[0].ZipOrPostalCode = input_message.MED[i].APM_Patient_Zip_Code
        output_rdeo11.PID.HomePhoneNumber[0].PhoneNumberString_DEPRECATED_FROM_2_3 = input_message.MED[i].APM_HomePhone

        if str_size(input_message.MED[i].APM_Email) > 0 and input_message.MED[i].APM_Email != "NULL":
            output_rdeo11.PID.HomePhoneNumber[0].EmailAddress = input_message.MED[i].APM_Email

        output_rdeo11.PID.PatientAccountNumber.IDNumber = defaultModifier + input_message.MED[i].EncounterID

        if str_to_lower(input_message.MED[i].OrderStatusName) == "active":
            sPriority = "R"  # routine
            giNonActive = 99
        else:
            sPriority = "H"  # historical med
            giNonActive = (str_to_int(str_numbers(input_message.MED[i].APM_MRN)) // 10) % 3

        output_rdeo11.Order[0].ORC.OrderControl = "NW"

        if (str_size(str_trim(input_message.MED[i].PrescriptionNumber)) > 2 and
                str_to_upper(str_trim(input_message.MED[i].PrescriptionNumber)) != "NULL"):
            output_rdeo11.Order[0].ORC.FillerOrderNumber.EntityIdentifier = defaultModifier + "-" + input_message.MED[i].PrescriptionNumber
            output_rdeo11.Order[0].RXE.PrescriptionNumber = defaultModifier + "-" + input_message.MED[i].PrescriptionNumber
        else:
            if (str_size(str_trim(input_message.MED[i].OrderNumberEXT)) > 2 and
                    str_to_upper(str_trim(input_message.MED[i].OrderNumberEXT)) != "NULL"):
                output_rdeo11.Order[0].ORC.FillerOrderNumber.EntityIdentifier = defaultModifier + "-" + input_message.MED[i].OrderNumberEXT
                output_rdeo11.Order[0].RXE.PrescriptionNumber = defaultModifier + "-" + input_message.MED[i].OrderNumberEXT
            else:
                if (str_size(str_trim(input_message.MED[i].CurrentID)) > 0 and
                        str_to_upper(str_trim(input_message.MED[i].CurrentID)) != "NULL"):
                    output_rdeo11.Order[0].ORC.FillerOrderNumber.EntityIdentifier = defaultModifier + "-" + input_message.MED[i].CurrentID
                    output_rdeo11.Order[0].RXE.PrescriptionNumber = defaultModifier + "-" + input_message.MED[i].CurrentID
                else:
                    gbValidMsg = False

        if gbValidMsg:
            output_rdeo11.Order[0].ORC.FillerOrderNumber.EntityIdentifier += "-" + \
                str_trim(input_message.MED[i].MedicationNDC_Code) + "-" + str_right(input_message.MED[i].APM_MRN, 5)
            output_rdeo11.Order[0].RXE.PrescriptionNumber += "-" + \
                str_trim(input_message.MED[i].MedicationNDC_Code) + "-" + str_right(input_message.MED[i].APM_MRN, 5)

        # Therapy Start Date-Time Hierarchy
        if (str_size(input_message.MED[i].TherapyStartedDTTM) > 0 and
                input_message.MED[i].TherapyStartedDTTM != "NULL" and
                str_left(input_message.MED[i].TherapyStartedDTTM, 2) != "21" and
                str_left(input_message.MED[i].TherapyStartedDTTM, 4) != "1900"):
            if str_mid(input_message.MED[i].TherapyStartedDTTM, 11, 8) == "00:00:00":
                set_encoded_value(output_rdeo11.Order[0].ORC.QuantityTiming[0].StartDateTime,
                                  date_change_format(str_left(input_message.MED[i].TherapyStartedDTTM, 10), "yyyy-MM-dd", "yyyyMMdd"))
                set_encoded_value(output_rdeo11.Order[0].RXE.QuantityTiming.StartDateTime,
                                  date_change_format(str_left(input_message.MED[i].TherapyStartedDTTM, 10), "yyyy-MM-dd", "yyyyMMdd"))
            else:
                set_encoded_value(output_rdeo11.Order[0].ORC.QuantityTiming[0].StartDateTime,
                                  date_change_format(str_left(input_message.MED[i].TherapyStartedDTTM, 19), "yyyy-MM-dd HH:mm:ss", "HL7"))
                set_encoded_value(output_rdeo11.Order[0].RXE.QuantityTiming.StartDateTime,
                                  date_change_format(str_left(input_message.MED[i].TherapyStartedDTTM, 19), "yyyy-MM-dd HH:mm:ss", "HL7"))
        else:
            if (str_size(input_message.MED[i].PerformedDTTM) > 0 and
                    input_message.MED[i].PerformedDTTM != "NULL" and
                    str_left(input_message.MED[i].PerformedDTTM, 2) != "21" and
                    str_left(input_message.MED[i].PerformedDTTM, 4) != "1900"):
                if str_mid(input_message.MED[i].PerformedDTTM, 11, 8) == "00:00:00":
                    set_encoded_value(output_rdeo11.Order[0].ORC.QuantityTiming[0].StartDateTime,
                                      date_change_format(str_left(input_message.MED[i].PerformedDTTM, 10), "yyyy-MM-dd", "yyyyMMdd"))
                    set_encoded_value(output_rdeo11.Order[0].RXE.QuantityTiming.StartDateTime,
                                      date_change_format(str_left(input_message.MED[i].PerformedDTTM, 10), "yyyy-MM-dd", "yyyyMMdd"))
                else:
                    set_encoded_value(output_rdeo11.Order[0].ORC.QuantityTiming[0].StartDateTime,
                                      date_change_format(str_left(input_message.MED[i].PerformedDTTM, 19), "yyyy-MM-dd HH:mm:ss", "HL7"))
                    set_encoded_value(output_rdeo11.Order[0].RXE.QuantityTiming.StartDateTime,
                                      date_change_format(str_left(input_message.MED[i].PerformedDTTM, 19), "yyyy-MM-dd HH:mm:ss", "HL7"))
            else:
                if (str_size(input_message.MED[i].TherapyEndDTTM) > 0 and
                        input_message.MED[i].TherapyEndDTTM != "NULL" and
                        str_left(input_message.MED[i].TherapyEndDTTM, 2) != "21" and
                        str_left(input_message.MED[i].TherapyEndDTTM, 4) != "1900"):
                    if str_mid(input_message.MED[i].TherapyEndDTTM, 11, 8) == "00:00:00":
                        set_encoded_value(output_rdeo11.Order[0].ORC.QuantityTiming[0].StartDateTime,
                                          date_change_format(str_left(input_message.MED[i].TherapyEndDTTM, 10), "yyyy-MM-dd", "yyyyMMdd"))
                        set_encoded_value(output_rdeo11.Order[0].RXE.QuantityTiming.StartDateTime,
                                          date_change_format(str_left(input_message.MED[i].TherapyEndDTTM, 10), "yyyy-MM-dd", "yyyyMMdd"))
                    else:
                        set_encoded_value(output_rdeo11.Order[0].ORC.QuantityTiming[0].StartDateTime,
                                          date_change_format(str_left(input_message.MED[i].TherapyEndDTTM, 19), "yyyy-MM-dd HH:mm:ss", "HL7"))
                        set_encoded_value(output_rdeo11.Order[0].RXE.QuantityTiming.StartDateTime,
                                          date_change_format(str_left(input_message.MED[i].TherapyEndDTTM, 19), "yyyy-MM-dd HH:mm:ss", "HL7"))
                else:
                    if (str_size(input_message.MED[i].ClinicalDTTM) > 0 and
                            input_message.MED[i].ClinicalDTTM != "NULL" and
                            str_left(input_message.MED[i].ClinicalDTTM, 2) != "21" and
                            str_left(input_message.MED[i].ClinicalDTTM, 4) != "1900"):
                        set_encoded_value(output_rdeo11.Order[0].ORC.QuantityTiming[0].StartDateTime,
                                          date_change_format(str_left(input_message.MED[i].ClinicalDTTM, 19), "yyyy-MM-dd HH:mm:ss", "yyyyMMddHHmm"))
                        set_encoded_value(output_rdeo11.Order[0].RXE.QuantityTiming.StartDateTime,
                                          date_change_format(str_left(input_message.MED[i].ClinicalDTTM, 19), "yyyy-MM-dd HH:mm:ss", "yyyyMMddHHmm"))
                    else:
                        set_encoded_value(output_rdeo11.Order[0].ORC.QuantityTiming[0].StartDateTime,
                                          date_change_format(current_date_time(True), "MM/dd/yyyy HH:mm:ss", "yyyyMMddHHmm"))
                        set_encoded_value(output_rdeo11.Order[0].RXE.QuantityTiming.StartDateTime,
                                          date_change_format(current_date_time(True), "MM/dd/yyyy HH:mm:ss", "yyyyMMddHHmm"))

        if (str_size(input_message.MED[i].TherapyEndDTTM) > 0 and
                input_message.MED[i].TherapyEndDTTM != "NULL" and
                str_left(input_message.MED[i].TherapyEndDTTM, 2) != "21" and
                str_left(input_message.MED[i].TherapyEndDTTM, 4) != "1900"):
            if str_mid(input_message.MED[i].TherapyEndDTTM, 11, 8) == "00:00:00":
                set_encoded_value(output_rdeo11.Order[0].ORC.QuantityTiming[0].EndDateTime,
                                  date_change_format(str_left(input_message.MED[i].TherapyEndDTTM, 10), "yyyy-MM-dd", "yyyyMMdd"))
                set_encoded_value(output_rdeo11.Order[0].RXE.QuantityTiming.EndDateTime,
                                  date_change_format(str_left(input_message.MED[i].TherapyEndDTTM, 10), "yyyy-MM-dd", "yyyyMMdd"))
            else:
                set_encoded_value(output_rdeo11.Order[0].ORC.QuantityTiming[0].EndDateTime,
                                  date_change_format(str_left(input_message.MED[i].TherapyEndDTTM, 19), "yyyy-MM-dd HH:mm:ss", "HL7"))
                set_encoded_value(output_rdeo11.Order[0].RXE.QuantityTiming.EndDateTime,
                                  date_change_format(str_left(input_message.MED[i].TherapyEndDTTM, 19), "yyyy-MM-dd HH:mm:ss", "HL7"))
        else:
            if giNonActive != 99:
                if (str_size(input_message.MED[i].ClinicalDTTM) > 0 and
                        input_message.MED[i].ClinicalDTTM != "NULL" and
                        str_left(input_message.MED[i].ClinicalDTTM, 2) != "21" and
                        str_left(input_message.MED[i].ClinicalDTTM, 4) != "1900"):
                    set_encoded_value(output_rdeo11.Order[0].ORC.QuantityTiming[0].EndDateTime,
                                      date_change_format(str_left(input_message.MED[i].ClinicalDTTM, 19), "yyyy-MM-dd HH:mm:ss", "yyyyMMddHHmm"))
                    set_encoded_value(output_rdeo11.Order[0].RXE.QuantityTiming.EndDateTime,
                                      date_change_format(str_left(input_message.MED[i].ClinicalDTTM, 19), "yyyy-MM-dd HH:mm:ss", "yyyyMMddHHmm"))
                else:
                    set_encoded_value(output_rdeo11.Order[0].ORC.QuantityTiming[0].EndDateTime,
                                      date_change_format(current_date_time(True), "MM/dd/yyyy HH:mm:ss", "yyyyMMddHHmm"))
                    set_encoded_value(output_rdeo11.Order[0].RXE.QuantityTiming.EndDateTime,
                                      date_change_format(current_date_time(True), "MM/dd/yyyy HH:mm:ss", "yyyyMMddHHmm"))

        sStartDttm = get_encoded_value(output_rdeo11.Order[0].ORC.QuantityTiming[0].StartDateTime)
        sEndDttm = get_encoded_value(output_rdeo11.Order[0].ORC.QuantityTiming[0].EndDateTime)

        if str_size(sStartDttm) == 8:
            sStartDttm += "000000"

        if str_size(sEndDttm) == 8:
            sEndDttm += "000000"

        if str_size(sEndDttm) > 0 and str_to_dbl(sStartDttm) > str_to_dbl(sEndDttm):
            set_encoded_value(output_rdeo11.Order[0].ORC.QuantityTiming[0].StartDateTime,
                              get_encoded_value(output_rdeo11.Order[0].ORC.QuantityTiming[0].EndDateTime))
            set_encoded_value(output_rdeo11.Order[0].RXE.QuantityTiming.StartDateTime,
                              get_encoded_value(output_rdeo11.Order[0].ORC.QuantityTiming[0].EndDateTime))

        if str_size(input_message.MED[i].OrderPriorityName) > 0:
            output_rdeo11.Order[0].ORC.QuantityTiming[0].Priority = input_message.MED[i].OrderPriorityName
            output_rdeo11.Order[0].RXE.QuantityTiming.Priority = input_message.MED[i].OrderPriorityName
        else:
            output_rdeo11.Order[0].ORC.QuantityTiming[0].Priority = sPriority
            output_rdeo11.Order[0].RXE.QuantityTiming.Priority = sPriority

        if input_message.MED[i].PRNFlag == "Y":
            if str_size(input_message.MED[i].PRN) > 0:
                output_rdeo11.Order[0].ORC.QuantityTiming[0].Condition = input_message.MED[i].PRN
                output_rdeo11.Order[0].RXE.QuantityTiming.Condition = input_message.MED[i].PRN
            else:
                output_rdeo11.Order[0].ORC.QuantityTiming[0].Condition = "PRN"
                output_rdeo11.Order[0].RXE.QuantityTiming.Condition = "PRN"

        if (str_size(input_message.MED[i].CreatedDTTM) > 0 and
                input_message.MED[i].CreatedDTTM != "NULL" and
                str_left(input_message.MED[i].CreatedDTTM, 4) != "1900"):
            if str_mid(input_message.MED[i].CreatedDTTM, 11, 8) == "00:00:00":
                set_encoded_value(output_rdeo11.Order[0].ORC.DateTimeOfTransaction,
                                  date_change_format(str_left(input_message.MED[i].CreatedDTTM, 10), "yyyy-MM-dd", "yyyyMMdd"))
            else:
                set_encoded_value(output_rdeo11.Order[0].ORC.DateTimeOfTransaction,
                                  date_change_format(str_left(input_message.MED[i].CreatedDTTM, 19), "yyyy-MM-dd HH:mm:ss", "HL7"))

            sNonActiveDTTM = date_change_format(str_left(input_message.MED[i].CreatedDTTM, 19), "yyyy-MM-dd HH:mm:ss", "MM/dd/yyyy hh:mma")
        else:
            if (str_size(input_message.MED[i].ClinicalDTTM) > 0 and
                    input_message.MED[i].ClinicalDTTM != "NULL" and
                    str_left(input_message.MED[i].ClinicalDTTM, 4) != "1900"):
                if str_mid(input_message.MED[i].ClinicalDTTM, 11, 8) == "00:00:00":
                    set_encoded_value(output_rdeo11.Order[0].ORC.DateTimeOfTransaction,
                                      date_change_format(str_left(input_message.MED[i].ClinicalDTTM, 10), "yyyy-MM-dd", "yyyyMMdd"))
                else:
                    set_encoded_value(output_rdeo11.Order[0].ORC.DateTimeOfTransaction,
                                      date_change_format(str_left(input_message.MED[i].ClinicalDTTM, 19), "yyyy-MM-dd HH:mm:ss", "HL7"))

                sNonActiveDTTM = date_change_format(str_left(input_message.MED[i].ClinicalDTTM, 19), "yyyy-MM-dd HH:mm:ss", "MM/dd/yyyy hh:mma")
            else:
                if (str_size(input_message.MED[i].LastUpdateDTTM) > 0 and
                        input_message.MED[i].LastUpdateDTTM != "NULL" and
                        str_left(input_message.MED[i].LastUpdateDTTM, 4) != "1900"):
                    if str_mid(input_message.MED[i].LastUpdateDTTM, 11, 8) == "00:00:00":
                        set_encoded_value(output_rdeo11.Order[0].ORC.DateTimeOfTransaction,
                                          date_change_format(str_left(input_message.MED[i].LastUpdateDTTM, 10), "yyyy-MM-dd", "yyyyMMdd"))
                    else:
                        set_encoded_value(output_rdeo11.Order[0].ORC.DateTimeOfTransaction,
                                          date_change_format(str_left(input_message.MED[i].LastUpdateDTTM, 19), "yyyy-MM-dd HH:mm:ss", "HL7"))

                    sNonActiveDTTM = date_change_format(str_left(input_message.MED[i].LastUpdateDTTM, 19), "yyyy-MM-dd HH:mm:ss", "MM/dd/yyyy hh:mma")

        if str_size(str_trim(input_message.MED[i].OrderingProviderNPI)) > 0:
            output_rdeo11.Order[0].ORC.OrderingProvider[0].IDNumber = str_trim(input_message.MED[i].OrderingProviderNPI)
            output_rdeo11.Order[0].ORC.OrderingProvider[0].FamilyName.Surname = input_message.MED[i].OrderingProviderLastName
            output_rdeo11.Order[0].ORC.OrderingProvider[0].GivenName = input_message.MED[i].OrderingProviderfirstName
            output_rdeo11.Order[0].ORC.OrderingProvider[0].AssigningAuthority.NamespaceID = "NPI"
            output_rdeo11.Order[0].ORC.OrderingProvider[0].IdentifierTypeCode = "NPI"
        else:
            output_rdeo11.Order[0].ORC.OrderingProvider[0].IDNumber = defaultProvID
            output_rdeo11.Order[0].ORC.OrderingProvider[0].FamilyName.Surname = defaultProvLName
            output_rdeo11.Order[0].ORC.OrderingProvider[0].GivenName = defaultProvFName
            output_rdeo11.Order[0].ORC.OrderingProvider[0].AssigningAuthority.NamespaceID = asgnAuth_OCMW_Provider
            output_rdeo11.Order[0].ORC.OrderingProvider[0].IdentifierTypeCode = idType_OCMW_Provider

        output_rdeo11.Order[0].RXE.GiveCode.Identifier = str_trim(input_message.MED[i].MedicationNDC_Code)
        output_rdeo11.Order[0].RXE.GiveCode.Text = input_message.MED[i].Medication
        output_rdeo11.Order[0].RXE.GiveCode.NameOfCodingSystem = "NDC"

        if str_size(input_message.MED[i].Dose) == str_size(str_numbers(input_message.MED[i].Dose)):
            output_rdeo11.Order[0].RXE.MinimumGiveAmount = str_to_dbl(input_message.MED[i].Dose)

            if output_rdeo11.Order[0].RXE.MinimumGiveAmount == 0:
                set_empty(output_rdeo11.Order[0].RXE.MinimumGiveAmount)
            else:
                if str_size(input_message.MED[i].UnitOfMeasure) > 0:
                    output_rdeo11.Order[0].RXE.GiveUnits.Identifier = str_to_lower(str_trim(input_message.MED[i].UnitOfMeasure))
        else:
            set_empty(output_rdeo11.Order[0].RXE.MinimumGiveAmount)
            set_empty(output_rdeo11.Order[0].RXE.MaximumGiveAmount)

        output_rdeo11.Order[0].RXE.ProvidersAdministrationInstructions[0].Text = input_message.MED[i].FreeTextSIG

        if str_size(input_message.MED[i].DAWFLAG) > 0:
            if input_message.MED[i].DAWFLAG == "Y":
                output_rdeo11.Order[0].RXE.SubstitutionStatus = "N"
            else:
                output_rdeo11.Order[0].RXE.SubstitutionStatus = "G"

        output_rdeo11.Order[0].RXE.DispenseAmount = str_to_dbl(input_message.MED[i].QuantityToDispense)

        if str_size(input_message.MED[i].PkgTxt) > 0 and input_message.MED[i].PkgTxt != "NULL":
            output_rdeo11.Order[0].RXE.DispenseUnits.Identifier = str_to_lower(input_message.MED[i].PkgTxt)
            output_rdeo11.Order[0].RXE.DispenseUnits.Text = input_message.MED[i].PkgTxt

        output_rdeo11.Order[0].RXE.NumberOfRefills = str_to_dbl(input_message.MED[i].Refill)

        if (str_size(input_message.MED[i].PerformedDTTM) > 0 and
                input_message.MED[i].PerformedDTTM != "NULL" and
                str_left(input_message.MED[i].PerformedDTTM, 4) != "1900"):
            if str_mid(input_message.MED[i].PerformedDTTM, 11, 8) == "00:00:00":
                set_encoded_value(output_rdeo11.Order[0].RXE.OriginalOrderDateTime,
                                  date_change_format(str_left(input_message.MED[0].PerformedDTTM, 10), "yyyy-MM-dd", "yyyyMMdd"))
            else:
                set_encoded_value(output_rdeo11.Order[0].RXE.OriginalOrderDateTime,
                                  date_change_format(str_left(input_message.MED[0].PerformedDTTM, 19), "yyyy-MM-dd HH:mm:ss", "HL7"))
        else:
            set_encoded_value(output_rdeo11.Order[0].RXE.OriginalOrderDateTime,
                              date_change_format(str_left(input_message.MED[0].ClinicalDTTM, 19), "yyyy-MM-dd HH:mm:ss", "HL7"))

        if str_size(str_trim(input_message.MED[i].FreqUnitsCode)) > 0:
            output_rdeo11.Order[0].TQ1.RepeatPattern[0].RepeatPatternCode.Identifier = str_trim(input_message.MED[i].FreqUnitsCode)

        if str_size(str_trim(input_message.MED[i].FreqUnitsName)) > 0:
            output_rdeo11.Order[0].TQ1.RepeatPattern[0].RepeatPatternCode.Text = str_trim(input_message.MED[i].FreqUnitsName)

        if input_message.MED[i].Refill != "0" and input_message.MED[i].DaysSupply != "0":
            output_rdeo11.Order[0].TQ1.ServiceDuration.Quantity = (str_to_dbl(input_message.MED[i].Refill) * str_to_dbl(input_message.MED[i].DaysSupply))
            output_rdeo11.Order[0].TQ1.ServiceDuration.Units.Identifier = "DAYS"
            output_rdeo11.Order[0].TQ1.ServiceDuration.Units.Text = "DAYS"

        output_rdeo11.Order[0].TQ1.ConditionText = input_message.MED[i].PRN

        if giNonActive != 99:
            output_rdeo11.Order[0].NTE[0].SetID = 1
            output_rdeo11.Order[0].NTE[0].SourceOfComment = defaultModifier
            output_rdeo11.Order[0].NTE[0].Comment[0] = f"Converted from {defaultModifier}: {input_message.MED[i].OrderStatusName} on {sNonActiveDTTM}"
            output_rdeo11.Order[0].NTE[0].CommentType.Identifier = "MN"

        output_rdeo11.Order[0].RXR.Route.Identifier = str_trim(input_message.MED[i].RouteofAdminCode)
        output_rdeo11.Order[0].RXR.Route.Text = str_trim(input_message.MED[i].RouteofAdminName)

        if str_size(input_message.MED[i].Diagnoses) > 0:
            diagnoses = input_message.MED[i].Diagnoses.split(";")
            for j, sDx in enumerate(diagnoses):
                output_rdeo11.Order[0].DG1[j].SetID = j + 1
                output_rdeo11.Order[0].DG1[j].DxCode.Identifier = sDx.split(" - ")[1]
                output_rdeo11.Order[0].DG1[j].DxCode.Text = str_trim(sDx.split(" - ")[0])
                output_rdeo11.Order[0].DG1[j].DxCode.NameOfCodingSystem = "I10"

        if input_message.MED[i].DaysToTake != "0":
            output_rdeo11.Order[0].ZXO.DaysInDurations.Text = input_message.MED[i].DaysToTake