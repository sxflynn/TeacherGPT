import { Title } from "@mantine/core";
import { DataTable } from '../components/DataTable'
import { GET_ALL_STUDENTS } from "../dataServices/students/queries";


const tableHeaders = {
  //   studentId: "Student ID",
  firstName: "First Name",
  middleName: "Middle Name",
  lastName: "Last Name",
  sex: "Sex",
  dob: "Date of Birth",
  email: "Email",
  ohioSsid: "Ohio SSID",
};

export function StudentPage() {
  
  return (
    <>
      <Title>Student Data</Title>
      <DataTable query={GET_ALL_STUDENTS} dataKey="allStudents" tableHeaders={tableHeaders} />
    </>
  );
}
