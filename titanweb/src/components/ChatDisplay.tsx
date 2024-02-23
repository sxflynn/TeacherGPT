import { Text, Paper } from "@mantine/core";


export function ChatDisplay({ data }: { data: string }) {
    return (
      <Paper>
        <Text>{data}</Text>
      </Paper>
    );
  }