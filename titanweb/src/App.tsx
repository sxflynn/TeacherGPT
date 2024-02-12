import "@mantine/core/styles.css";
import {
  AppShell,
  Burger,
  MantineProvider,
  localStorageColorSchemeManager,
} from "@mantine/core";
import { theme } from "./theme";
import { Outlet } from "react-router-dom";
import { useDisclosure } from "@mantine/hooks";
import { AppShellHeader } from "./components/AppShellHeader";
import { AppShellNavbar } from "./components/AppShellNavbar";

export default function App() {
  const [opened, { toggle }] = useDisclosure();

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
          width: 300,
          breakpoint: "sm",
          collapsed: { mobile: !opened },
        }}
        padding="md"
      >
        <AppShell.Header>
          <Burger opened={opened} onClick={toggle} hiddenFrom="sm" size="sm" />
          <AppShellHeader/>
        </AppShell.Header>

        <AppShell.Navbar p="md">
          <AppShellNavbar/>
          </AppShell.Navbar>
        

        <AppShell.Main>
        <Outlet />
        </AppShell.Main>
      </AppShell>
    </MantineProvider>
  );
}
