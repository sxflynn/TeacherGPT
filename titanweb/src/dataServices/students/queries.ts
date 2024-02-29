import { gql } from "@apollo/client"

export const GET_ALL_STUDENTS = gql`query StudentsListAll {
    studentsListAll {
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
