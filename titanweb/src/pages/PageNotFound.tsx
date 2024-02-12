import { Container, Title, Text, Button, Space } from "@mantine/core";
import { IconArrowLeftBar, IconError404 } from "@tabler/icons-react";
import { Link } from "react-router-dom";

const PageNotFound = () => {
  return (
    <Container size="30rem" mt="lg">
            <div>
                <IconError404 size={300} />
              <Title>Page not found</Title>
              <Text mt="md" c="dimmed" size="lg">
                Page you are trying to open does not exist. You may have mistyped
                the address, or the page has been moved to another URL.
              </Text>
              <Link to="/">
                <Button variant="outline" size="md" mt="xl">
                  <IconArrowLeftBar/><Space w="xs"></Space> Get back to home page
                </Button>
              </Link>
            </div>
    </Container>
  );
};

export default PageNotFound;