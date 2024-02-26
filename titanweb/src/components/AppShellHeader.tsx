import { Burger, Group, Title, Image } from "@mantine/core";
import { Dispatch, SetStateAction } from "react";
import { NavLink } from "react-router-dom";
import schoolLogo from "../assets/logo.svg";

type HeaderProps = {
  opened: boolean;
  toggle: () => void;
  setActive: Dispatch<SetStateAction<string>>;
};

export function AppShellHeader({ opened, toggle, setActive }: HeaderProps) {
  return (
    <>
      <Group justify="space-between">
        <Group>
          <Burger opened={opened} onClick={toggle} hiddenFrom="sm" size="sm" />
          <NavLink
            style={{ textDecoration: "none", color: "inherit" }}
            to="/"
            onClick={() => setActive("")}
          >
            <Title order={4}>Titan Academy School Information System</Title>
          </NavLink>
        </Group>
          <Image pr="sm" pt="sm" height={50} src={schoolLogo} />
      </Group>
    </>
  );
}
