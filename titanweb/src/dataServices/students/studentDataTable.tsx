import {  useQuery } from "@apollo/client";
import { Table } from "@mantine/core";
import { GET_ALL_STUDENTS } from "./studentQuery";
import { studentMock } from "./studentMockData";


type GenericObject = { [key: string]: string };

const headersMapping: { [key: string]: string } = {
//   studentId: "Student ID",
  firstName: "First Name",
  middleName: "Middle Name",
  lastName: "Last Name",
  sex: "Sex",
  dob: "Date of Birth",
  email: "Email",
  ohioSsid: "Ohio SSID",
};

export function StudentDataTable() {

  const { loading, error, data } = useQuery(GET_ALL_STUDENTS);

  // const students = studentMock.data.allStudents;

  const students = data && data.allStudents ? data.allStudents : [];
  console.log("students is ", students)

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error : {error.message}</p>;

  const headers = Object.keys(headersMapping).map((key) => (
    <Table.Th key={key}>{headersMapping[key]}</Table.Th>
  ));

  // Generating table rows
  const rows = students.map((student, index) => (
    <Table.Tr key={index}>
      {Object.keys(headersMapping).map((key) => (
        <Table.Td key={`${key}-${index}`}>{student[key]}</Table.Td>
      ))}
    </Table.Tr>
  ));

  return (
    <Table>
      <Table.Thead>
        <Table.Tr>{headers}</Table.Tr>
      </Table.Thead>
      <Table.Tbody>{rows}</Table.Tbody>
    </Table>
  );
}
