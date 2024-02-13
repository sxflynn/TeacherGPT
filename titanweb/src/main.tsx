import React from "react";
import ReactDOM from "react-dom/client";
import {
  createBrowserRouter,
  RouterProvider,
  createRoutesFromElements,
  Route,
} from "react-router-dom";
import App from "./App.tsx";
import { Homepage } from "./pages/Homepage.tsx";
import PageNotFound from "./pages/PageNotFound.tsx";
import { StudentPage } from "./pages/StudentPage.tsx";

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route path="/" element={<App />}>
      <Route index element={<Homepage />} />{" "}
      <Route path="students" element={<StudentPage/>}/>
      <Route path="*" element={<PageNotFound />} />
    </Route>
  )
);


ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
