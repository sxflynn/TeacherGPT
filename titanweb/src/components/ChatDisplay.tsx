import { List, ListItem, Text } from "@mantine/core";

const parseContent = (content: string) => {
  const elements: React.ReactNode[] = [];
  const lines = content.split("\n");
  let currentListItems: string[] = [];
  let isOrderedList = false;

  const renderList = () => {
    if (currentListItems.length > 0) {
      const listElements = currentListItems.map((item, listItemIndex) => (
        <ListItem key={`list-item-${elements.length}-${listItemIndex}`}>
          {item}
        </ListItem>
      ));
      elements.push(
        <List
          withPadding
          type={isOrderedList ? "ordered" : "unordered"}
          key={`list-${elements.length}`}
        >
          {listElements}
        </List>
      );
      currentListItems = [];
      isOrderedList = false;
    }
  };

  lines.forEach((line) => {
    const bulletListMatch = line.match(/^(?:[*-])\s(.*)/);
    const orderedListMatch = line.match(/^(\d+)\.\s(.*)/);

    if (bulletListMatch) {
      isOrderedList = false;
      currentListItems.push(bulletListMatch[1]); // Safe to access since we checked it's not null
    } else if (orderedListMatch) {
      isOrderedList = true;
      currentListItems.push(orderedListMatch[2]); // Safe to access since we checked it's not null
    } else {
      renderList();

      if (line.trim() !== "") {
        elements.push(<Text key={`text-${elements.length}`}>{line}</Text>);
      }
    }
  });

  renderList();

  return elements;
};

type ChatDisplayProps = {
  data: string[];
};

export function ChatDisplay({ data }: ChatDisplayProps) {
  const combinedData = data.join("");
  const contentElements = parseContent(combinedData);

  return <>{contentElements}</>;
}
