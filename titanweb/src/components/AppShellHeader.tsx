import { Burger, Title } from "@mantine/core";
import { Dispatch, SetStateAction } from "react";
import { NavLink } from "react-router-dom";

type HeaderProps = {
  opened: boolean
  toggle:() => void
  setActive: Dispatch<SetStateAction<string>>;
};


export function AppShellHeader({opened, toggle, setActive}:HeaderProps) {
  return (
   <>
      <Burger opened={opened} onClick={toggle} hiddenFrom="sm" size="sm" />
      <NavLink style={{ textDecoration: "none", color: "inherit" }} to="/" onClick={() => setActive("")}>
        <Title order={4}>Titan Academy School Information System</Title>
      </NavLink>
   </>
  );
}
