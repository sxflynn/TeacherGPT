import { Title } from "@mantine/core";
import { CustomDataTable } from '../components/CustomDataTable'
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
      <CustomDataTable query={GET_ALL_STUDENTS} dataKey="studentsListAll" tableHeaders={tableHeaders} />
    </>
  );
}
