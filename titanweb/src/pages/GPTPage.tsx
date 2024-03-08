import {
  Box,
  Button,
  Group,
  TextInput,
  Title,
  Notification,
  Paper,
  Skeleton,
} from "@mantine/core";
import { useForm } from "@mantine/form";
import { useState } from "react";
import { Error } from "../components/Error";
import { ChatDisplay } from "../components/ChatDisplay";

type FormInput = {
  prompt: string;
};

export function GPTPage() {
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

    const devMode: boolean = import.meta.env.VITE_DEV_MODE === "true";
    const chatLogicPort: string = import.meta.env.VITE_CHATLOGIC_PORT_DEVMODE;
    let baseUrl: string;
    const protocol: string =
      window.location.protocol === "https:" ? "wss" : "ws";

    if (devMode) {
      baseUrl = `${protocol}://${window.location.hostname}:${chatLogicPort}`;
    } else {
      const chatLogicBaseUrl: string =
        import.meta.env.VITE_CHATLOGIC_BASE_URL.replace(/^http(s?):\/\//, "");
      baseUrl = `${protocol}://${chatLogicBaseUrl}`;
    }

    const ws = new WebSocket(`${baseUrl}/promptstreaming`);

    ws.onopen = () => {
      ws.send(JSON.stringify(values));
    };

    ws.onmessage = (event) => {
      setStreamingResponses((currentResponses) => [
        ...currentResponses,
        event.data,
      ]);
    };

    ws.onerror = (event) => {
      const url = event?.target?.url;
      const errorMessage = url
        ? `Unable to connect to ${url}`
        : "Unable to connect to the WebSocket server.";
      setError(errorMessage);
      console.error("WebSocket error observed:", event, `URL: ${url}`);
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
            <Button type="submit" disabled={loading} mt="sm">
              Submit Prompt
            </Button>

            {loading && (
              <Notification
                style={{ boxShadow: "none" }}
                mt="sm"
                withCloseButton={false}
                loading
                title="Generating text"
              />
            )}
          </Group>

          {error && <Error error={error} onDismiss={() => setError(null)} />}
        </form>
      </Box>

      {streamingResponses.length < 1 && loading && (
        <Paper p="md" withBorder>
          <Skeleton mt={6} height={12} radius="xl" />
          <Skeleton mt={6} height={12} radius="xl" />
        </Paper>
      )}

      {streamingResponses.length > 0 && (
        <Paper p="md" withBorder>
          <ChatDisplay data={streamingResponses} />
        </Paper>
      )}
    </>
  );
}
