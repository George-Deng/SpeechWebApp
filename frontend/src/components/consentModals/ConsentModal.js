import React from 'react'
import Modal from '../Modal/Modal'
import classes from './ConsentModal.module.css'
import Card from '../ui/Card'
/*
displays hipaa consent form 
*/
export default function ConsentModal() {
    return (
        <li className={classes.item}>
        <Card>
            <Modal>
                <div className={classes.modalbody}>
                    <p>
                                The Health Insurance Portability and Accountability Act (HIPAA) provides safeguards to protect your privacy. 
                    Implementation of HIPAA requirements officially began on April 14, 2003. Many of the policies have been our
                    practice for years. This form is a “friendly” version. A more complete text is posted in the office.
                    What this is all about: Specifically, there are rules and restrictions on who may see or be notified of your 
                    Protected Health Information (PHI). These restrictions do not include the normal interchange of information 
                    necessary to provide you with office services. HIPAA provides certain rights and protections to you as the 
                    patient. We balance these needs with our goal of providing you with quality professional service and care. 
                    Additional information is available from the U.S. Department of Health and Human Services. www.hhs.gov
                    We have adopted the following policies:
                    1. Patient information will be kept confidential except as is necessary to provide services or to ensure that all 
                    administrative matters related to your care are handled appropriately. This specifically includes the sharing of 
                    information with other healthcare providers, laboratories, health insurance payers as is necessary and appropriate 
                    for your care. Patient files may be stored in open file racks and will not contain any coding which identifies a 
                    patient’s condition or information which is not already a matter of public record. The normal course of providing 
                    care means that such records may be left, at least temporarily, in administrative areas such as the front office, 
                    examination room, etc. Those records will not be available to persons other than office staff . You agree to the 
                    normal procedures utilized within the office for the handling of charts, patient records, PHI and other documents 
                    or information.
                    2. It is the policy of this office to remind patients of their appointments. We may do this by telephone, e-mail, 
                    U.S mail, or by any means convenient for the practice and/or as requested by you. We may send you other 
                    communications informing you of changes to office policy and new technology that you might find valuable or 
                    informative.
                    3. The practice utilizes a number of vendors in the conduct of business. These vendors may have access to PHI 
                    but must agree to abide by the confidentiality rules of HIPAA.
                    4. You understand and agree to inspections of the office and review of documents which may include PHI by 
                    government agencies or insurance payers in normal performance of their duties.
                    5. You agree to bring any concerns or complaints regarding privacy to the attention of the office manger or the 
                    doctor.
                    6. Your confidential information will not be used for the purposes of marketing or advertising of products, goods 
                    or services.
                    7. We agree to provide patients with access to their records in accordance with state and federal laws.
                    8. We may change, add, delete or modify any of these provisions to better serve the needs of the both the 
                    practice and the patient.
                    9. You have the right to request restrictions in the use of your protected health information and to request change 
                    in certain policies used within the office concerning your PHI. However, we are not obligated to alter internal 
                    policies to conform to your request
                    </p>
                </div>
          </Modal>
        </Card>
      
    </li>
    )
}
