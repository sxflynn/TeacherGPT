import { Text, Paper } from "@mantine/core";

export type ChatResponse = { response : string}

export function ChatDisplay({ data }: { data: ChatResponse }) {
    return (
      <Paper>
        <Text>{data.response}</Text>
      </Paper>
    );
  }