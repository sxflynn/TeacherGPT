import { NavLink } from "@mantine/core";
import { IconFidgetSpinner, IconMessageCircle, IconUser,IconTallymarks } from "@tabler/icons-react";
import { Dispatch, SetStateAction } from "react";
import { Link } from "react-router-dom";


type NavbarProps = {
  active: string;
  setActive: Dispatch<SetStateAction<string>>;
  toggle: () => void;
};

export function AppShellNavbar({active, setActive, toggle }:NavbarProps) {

  const links = [
    {link: "/gpt", label:"TeacherGPT", icon: IconMessageCircle},
    { link: "/students", label: "Students", icon: IconFidgetSpinner },
    { link: "/staff", label: "Staff", icon: IconTallymarks },
    { link: "/attendance", label: "Attendance", icon: IconUser },
  ];

  const navLinks = links.map((link) => {
    return (
        <NavLink
          component={Link}
          to={link.link}
          key={link.label}
          label={link.label}
          data-active={active === link.link || null}
          onClick={() => { setActive(link.link); toggle(); }}
          leftSection={link.icon ? <link.icon /> : null}
        />
    );
  });

  return (
    <>
    {navLinks}
    </>


  );
}
