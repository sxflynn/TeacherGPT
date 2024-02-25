import { NavLink } from "@mantine/core";
import { IconFidgetSpinner, IconMessageCircle, IconUser } from "@tabler/icons-react";
import { Dispatch, SetStateAction } from "react";
import { Link } from "react-router-dom";


type NavbarProps = {
  active: string
  setActive: Dispatch<SetStateAction<string>>;
};

export function AppShellNavbar({active, setActive}:NavbarProps) {

  const links = [
    {link: "/gpt", label:"TeacherGPT", icon: IconMessageCircle},
    { link: "/students", label: "Students", icon: IconFidgetSpinner },
    { link: "/Staff", label: "Staff", icon: IconUser },
  ];

  const navLinks = links.map((link) => {
    return (
        <NavLink
          component={Link}
          to={link.link}
          key={link.label}
          label={link.label}
          data-active={active === link.link || null}
          onClick={() => setActive(link.link)}
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
