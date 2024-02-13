import { Title } from "@mantine/core";
import { NavLink } from "react-router-dom";


export function AppShellHeader() {
  return (

    <NavLink
      to="/"
    >
      <Title
      >Titan Academy School Information System</Title>
    </NavLink>
  );
}
