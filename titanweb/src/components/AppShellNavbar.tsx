import { NavLink } from "@mantine/core";
import { IconFidgetSpinner, IconMessage, IconMessageCircle, IconUser } from "@tabler/icons-react";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

export function AppShellNavbar() {
  const [active, setActive] = useState(location.pathname);

  useEffect(() => {
    setActive(location.pathname);
  }, [location]);

  const links = [
    {link: "/gpt", label:"TeacherGPT", icon: IconMessageCircle},
    { link: "/gptstreaming", label: "StreamingGPT", icon:IconMessage},
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
          data-active={active === link.link || undefined}
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
