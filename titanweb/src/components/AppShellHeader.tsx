import { Title } from "@mantine/core";
import { Dispatch, SetStateAction } from "react";
import { NavLink } from "react-router-dom";

type HeaderProps = {
  setActive: Dispatch<SetStateAction<string>>;
};


export function AppShellHeader({setActive}:HeaderProps) {
  return (
    <NavLink style={{ textDecoration: "none", color: "inherit" }} to="/" onClick={() => setActive("")}>
      <Title>Titan Academy School Information System</Title>
    </NavLink>
  );
}
