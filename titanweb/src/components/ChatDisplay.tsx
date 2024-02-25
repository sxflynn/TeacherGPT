import { List, ListItem, Text } from '@mantine/core';

const parseContent = (content) => {
  const elements = [];
  const lines = content.split("\n");
  let currentListItems = [];
  let isOrderedList = false;

  // Function to render and reset the current list
  const renderList = () => {
    if (currentListItems.length > 0) {
      const listElements = currentListItems.map((item, listItemIndex) => (
        <ListItem key={`list-item-${elements.length}-${listItemIndex}`}>{item}</ListItem>
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

    if (bulletListMatch || orderedListMatch) {
      if (orderedListMatch) {
        isOrderedList = true;
        currentListItems.push(orderedListMatch[2]);
      } else {
        isOrderedList = false;
        currentListItems.push(bulletListMatch[1]);
      }
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

export function ChatDisplay({ data }) {
  const combinedData = data.join(""); // Ensure each data element starts on a new line
  const contentElements = parseContent(combinedData);

  return <>{contentElements}</>;
}
