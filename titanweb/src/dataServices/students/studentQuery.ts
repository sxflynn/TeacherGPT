import { gql } from "@apollo/client"

export const GET_ALL_STUDENTS = gql`query AllStudents {
    allStudents {
        studentId
        firstName
        middleName
        lastName
        sex
        dob
        email
        ohioSsid
    }
}
`;
