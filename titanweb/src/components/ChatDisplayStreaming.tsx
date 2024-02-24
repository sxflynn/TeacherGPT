import { Text, Paper } from "@mantine/core";

export type ChatResponse = { response : string}

export function ChatDisplayStreaming({ data }: { data: ChatResponse }) {
    return (
      <Paper>
        <Text>{data.response}</Text>
      </Paper>
    );
  }