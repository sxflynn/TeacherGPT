import { CodeHighlight } from "@mantine/code-highlight";
import { Text, Paper, List, ListItem } from "@mantine/core";

const parseContent = (content: string) => {
  const lines = content.split("\n");
  const contentElements = [];
  let currentListItems: string[] = [];
  let currentCodeLines: string[] = [];
  let isOrderedList = false;
  let isCodeBlock = false;
  let codeLanguage = "txt";

  lines.forEach((line, index) => {
    if (!isCodeBlock && line.startsWith("```")) {
      isCodeBlock = true;
      const languageMatch = line.match(/^```(\w+)?/);
      codeLanguage =
        languageMatch && languageMatch[1] ? languageMatch[1] : "txt";
      return;
    }

    if (isCodeBlock && line === "```") {
      isCodeBlock = false;
      contentElements.push(
        <CodeHighlight
          bg="lightgrey"
          m={10}
          p={10}
          withCopyButton={true}
          code={currentCodeLines.join("\n")}
          language={codeLanguage}
          key={`code-${index}`}
        />
      );
      currentCodeLines = [];
      codeLanguage = "txt";
      return;
    }

    if (isCodeBlock) {
      currentCodeLines.push(line);
      return;
    }

    const orderedListMatch = line.match(/^(\d+)\./);
    if (orderedListMatch) {
      if (isOrderedList === false && currentListItems.length > 0) {
        contentElements.push(
          <List withPadding type="unordered" key={`list-${index}`}>
            {currentListItems.map((item, key) => (
              <ListItem key={key}>{item}</ListItem>
            ))}
          </List>
        );
        currentListItems = [];
      }
      isOrderedList = true;
      currentListItems.push(line.substring(orderedListMatch[0].length).trim());
      return;
    }

    const bulletListMatch = line.match(/^(?:[*-])\s/);
    if (bulletListMatch) {
      if (isOrderedList === true && currentListItems.length > 0) {
        contentElements.push(
          <List withPadding type="ordered" key={`list-${index}`}>
            {currentListItems.map((item, key) => (
              <ListItem key={key}>{item}</ListItem>
            ))}
          </List>
        );
        currentListItems = [];
      }
      isOrderedList = false;
      currentListItems.push(line.substring(bulletListMatch[0].length).trim());
      return;
    }

    if (!isCodeBlock && currentListItems.length > 0 && line.trim() === "") {
      contentElements.push(
        <List
          withPadding
          type={isOrderedList ? "ordered" : "unordered"}
          key={`list-${index}`}
        >
          {currentListItems.map((item, key) => (
            <ListItem key={key}>{item}</ListItem>
          ))}
        </List>
      );
      currentListItems = [];
      isOrderedList = false;
    }

    if (
      !isCodeBlock &&
      !orderedListMatch &&
      !bulletListMatch &&
      line.trim() !== ""
    ) {
      contentElements.push(<Text key={`text-${index}`}>{line}</Text>);
    }
  });

  if (currentListItems.length > 0) {
    contentElements.push(
      <List
        withPadding
        type={isOrderedList ? "ordered" : "unordered"}
        key="final-list"
      >
        {currentListItems.map((item, key) => (
          <ListItem key={key}>{item}</ListItem>
        ))}
      </List>
    );
  }

  if (currentCodeLines.length > 0) {
    contentElements.push(
      <CodeHighlight
        withCopyButton={true}
        bg="grey"
        code={currentCodeLines.join("\n")}
        language={codeLanguage}
        key="final-code"
      />
    );
  }

  return contentElements;
};

export function ChatDisplayStreaming({ data }: { data: string[] }) {
  const combinedData = data.join("");
  const contentElements = parseContent(combinedData);

  return (
    <Paper p="md" withBorder>
      {contentElements}
    </Paper>
  );
}
