import React from "react";
import ReactDOM from "react-dom/client";
import {
  createBrowserRouter,
  RouterProvider,
  createRoutesFromElements,
  Route,
} from "react-router-dom";
import App from "./App.tsx";
import {
  ApolloClient,
  InMemoryCache,
  ApolloProvider,
} from "@apollo/client";
import { Homepage } from "./pages/Homepage.tsx";
import { GPTPage } from "./pages/GPTPage.tsx";
import { StaffPage } from "./pages/StaffPage.tsx";
import PageNotFound from "./pages/PageNotFound.tsx";
import { StudentPage } from "./pages/StudentPage.tsx";
import { AttendancePage } from "./pages/AttendancePage.tsx";
import { StudentPageNew } from "./pages/StudentPageNew.tsx";

const devMode:boolean = import.meta.env.VITE_DEV_MODE === 'true';
const gqlPort = import.meta.env.VITE_GRAPHQL_PORT_DEVMODE;
let gqlBaseUrl:string;
const protocol = window.location.protocol.includes('https') ? 'https' : 'http';

if (devMode) {
  gqlBaseUrl = `${protocol}://${window.location.hostname}:${gqlPort}`;
} else {
  gqlBaseUrl = `${protocol}://${import.meta.env.VITE_GRAPHQL_BASE_URL}`;
}

console.log(gqlBaseUrl)
const client = new ApolloClient({
  uri: `${gqlBaseUrl}/graphql`,
  cache: new InMemoryCache(),
});

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route path="/" element={<App />}>
      <Route index element={<Homepage />} />{" "}
      <Route path="students" element={<StudentPage />} />
      <Route path="studentsnew" element={<StudentPageNew />} />
      <Route path="staff" element={<StaffPage />} />
      <Route path="gpt" element={<GPTPage />} />
      <Route path="attendance" element={<AttendancePage />} />
      <Route path="*" element={<PageNotFound />} />
    </Route>
  )
);

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <React.StrictMode>
    <ApolloProvider client={client}>
      <RouterProvider router={router} />
    </ApolloProvider>
  </React.StrictMode>
);
