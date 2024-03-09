import "@mantine/core/styles.css";
import {
  AppShell,
  MantineProvider,
  localStorageColorSchemeManager,
} from "@mantine/core";
import { theme } from "./theme";
import { Outlet, useLocation } from "react-router-dom";
import { useDisclosure } from "@mantine/hooks";
import { AppShellHeader } from "./components/AppShellHeader";
import { AppShellNavbar } from "./components/AppShellNavbar";
import { useEffect, useState } from "react";

import 'mantine-datatable/styles.layer.css';
import './layout.css';

export default function App() {
  const location = useLocation();
  const [opened, { toggle }] = useDisclosure();
  const [active, setActive] = useState(location.pathname);
  
  useEffect(() => {
    setActive(location.pathname);
  }, [location.pathname]);
  
  return (
    <MantineProvider
      theme={theme}
      defaultColorScheme="auto"
      colorSchemeManager={localStorageColorSchemeManager({
        key: "portfolio-color-scheme",
      })}
    >
      <AppShell
        header={{ height: 60 }}
        navbar={{
          width: 200,
          breakpoint: "sm",
          collapsed: { mobile: !opened },
        }}
        padding="md"
      >
        <AppShell.Header>
          <AppShellHeader toggle={toggle} opened={opened} setActive={setActive}/>
        </AppShell.Header>

        <AppShell.Navbar p="md">
          <AppShellNavbar active={active} setActive={setActive} toggle={toggle} />
          </AppShell.Navbar>
        

        <AppShell.Main>
        <Outlet />
        </AppShell.Main>
      </AppShell>
    </MantineProvider>
  );
}
