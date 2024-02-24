import { Box, Button, Group, TextInput, Title } from "@mantine/core";
import { useForm } from "@mantine/form";
import { useState } from "react";
import { Loading } from "../components/Loading/Loading";
import { Error } from "../components/Error";
import { ChatDisplayStreaming } from "../components/ChatDisplayStreaming";

type FormInput = {
  prompt: string;
};

export function GPTStreaming() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<null | string>(null);
  const [streamingResponses, setStreamingResponses] = useState<string[]>([]);

  const form = useForm<FormInput>({
    initialValues: {
      prompt: "",
    },
    validate: {
      prompt: (value: string) =>
        value.length === 0 ? "Please type a prompt" : null,
    },
  });

  const handleStreamingSubmit = (values: FormInput) => {
    setLoading(true);
    setError(null);
    setStreamingResponses([]);

    const baseUrl = import.meta.env.VITE_CHATLOGIC_BASE_URL.replace(
      /^http(s?):\/\//,
      ""
    ); // fixes ws:// prepend bug
    const ws = new WebSocket(`ws://${baseUrl}/promptstreaming`);
    ws.onopen = () => {
      ws.send(JSON.stringify(values));
    };

    ws.onmessage = (event) => {
      setStreamingResponses((currentResponses) => [
        ...currentResponses,
        event.data,
      ]);
      console.log("streamingResponses is ", streamingResponses);
    };

    ws.onerror = (event) => {
      setError("WebSocket error, check the console for more details");
      console.error(event);
    };

    ws.onclose = () => {
      setLoading(false);
    };
  };

  return (
    <>
      <Title order={3}>Teacher GPT</Title>
      <Box mb="md">
        <form onSubmit={form.onSubmit(handleStreamingSubmit)}>
          <TextInput
            label="Type your question"
            placeholder="What do you know about the student with the last name Bell?"
            {...form.getInputProps("prompt")}
          />
          <Group>
            <Button type="submit" disabled={loading} mt="md">
              Submit Prompt
            </Button>
            {loading && <Loading />}
          </Group>
          {error && <Error error={error} onDismiss={() => setError(null)} />}
        </form>
      </Box>
      {streamingResponses && <ChatDisplayStreaming data={streamingResponses} />}
    </>
  );
}
