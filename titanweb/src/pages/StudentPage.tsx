import { Title } from "@mantine/core";
import { StudentDataTable } from "../dataServices/students/studentDataTable";

export function StudentPage() {
  return (
    <>
      <Title>Student Data</Title>
      <StudentDataTable />
    </>
  );
}
