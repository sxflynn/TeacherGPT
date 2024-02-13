import { useQuery, DocumentNode } from "@apollo/client";
import { Table } from "@mantine/core";

type TableRow = { [key: string]: any };

type TableHeaders = { [key: string]: string };

type DataTableProps = {
  dataKey: string;
  tableHeaders: TableHeaders;
  query: DocumentNode;
};

export function DataTable({ dataKey, tableHeaders, query }: DataTableProps) {
  const { loading, error, data } = useQuery(query);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error : {error.message}</p>;

  const rowsData: TableRow[] = data && data[dataKey] ? data[dataKey] : [];

  const headers = Object.keys(tableHeaders).map((key) => (
    <Table.Th key={key}>{tableHeaders[key]}</Table.Th>
  ));

  // Generating table rows
  const rows = rowsData.map((item, index) => (
    <Table.Tr key={index}>
      {Object.keys(tableHeaders).map((key) => (
        <Table.Td key={`${key}-${index}`}>{item[key]}</Table.Td>
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
