import { Title } from "@mantine/core";
import { DataTable } from "mantine-datatable";
import { GET_ALL_STUDENTS } from "../dataServices/students/queries";
import { useQuery } from "@apollo/client";

export function StudentPageNew() {
  const { loading, error, data } = useQuery(GET_ALL_STUDENTS);

  const records = data?.studentsListAll ? data.studentsListAll : [];

  return (
    <>
      <Title>Student Data</Title>
      <DataTable
        withTableBorder
        minHeight={180}
        columns={[
          { accessor: "firstName" },
          { accessor: "middleName" },
          { accessor: "lastName" },
          { accessor: "sex" },
          { accessor: "dob" },
          { accessor: "email" },
          { accessor: "ohioSsid" },
        ]}
        records={records}
        fetching={loading}
        loaderType="oval"
        loaderBackgroundBlur={2}
      />
    </>
  );
}
