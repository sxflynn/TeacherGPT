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
    // Detect the start of a code block
    if (!isCodeBlock && line.startsWith("```")) {
      isCodeBlock = true;
      // Extract the language if provided, otherwise default to plaintext
      const languageMatch = line.match(/^```(\w+)?/);
      codeLanguage =
        languageMatch && languageMatch[1] ? languageMatch[1] : "txt";
      return;
    }

    // Detect the end of a code block
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
      codeLanguage = "txt"; // Reset to default 'plaintext'
      return;
    }

    // If we're in a code block, add the line to the code lines array
    if (isCodeBlock) {
      currentCodeLines.push(line);
      return;
    }

    // Handle ordered lists
    const orderedListMatch = line.match(/^(\d+)\./);
    if (orderedListMatch) {
      // Finalize the current list if needed
      if (isOrderedList === false && currentListItems.length > 0) {
        // Push the current unordered list to contentElements
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

    // Handle bullet point lists
    const bulletListMatch = line.match(/^(?:[*-])\s/);
    if (bulletListMatch) {
      // Finalize the current list if needed
      if (isOrderedList === true && currentListItems.length > 0) {
        // Push the current ordered list to contentElements
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
    // Finalize lists if we've reached the end of a list block
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

    // If the current line is not a list item or code, handle it as regular text
    if (
      !isCodeBlock &&
      !orderedListMatch &&
      !bulletListMatch &&
      line.trim() !== ""
    ) {
      contentElements.push(<Text key={`text-${index}`}>{line}</Text>);
    }
  });

  // Finalize any remaining lists
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

  // Finalize any remaining code blocks
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
