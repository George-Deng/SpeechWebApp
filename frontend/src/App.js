import { Route, Switch} from "react-router-dom";
import MainNavigation from "./components/layout/MainNavigation";
import LoginPage from "./pages/Login";
import HomePage from "./pages/Home";
import UploadHistory from "./pages/UploadHistory";
import PatientListPage from "./pages/PatientList";
import SignupPage from "./pages/Signup";
import Layout from "./components/ui/Layout";


//Defines all the routing for our website and which components to display at the predefined urls
function App() {
  return (

      <Switch>
        <Route path='/home' exact>
          <MainNavigation title = 'Home'/>
          <HomePage/>
        </Route>
    
        <Route path='/signUp' exact>
        <Layout>
          <SignupPage title = 'Sign Up'/>
          </Layout>
        </Route>

        <Route path='/' exact>
        <Layout>
          <LoginPage title = 'Login'/>
        </Layout>
        </Route>

        <Route path='/uploadHistory' exact>
        <MainNavigation title = 'Upload History'/>
        <Layout>
          <UploadHistory/>
        </Layout>

        </Route>
        <Route path='/patientList' exact>
        <MainNavigation title = 'Patient List'/>
          <Layout>
            <PatientListPage/>
          </Layout>
        </Route>
      </Switch>
  );
}

export default App;
