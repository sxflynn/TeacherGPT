import { Title } from "@mantine/core";
import { StudentTable } from "../components/DataTables/StudentTable";

export function StudentPage() {
  return (
    <>
      <Title>Student Data</Title>
      <StudentTable />
    </>
  );
}
