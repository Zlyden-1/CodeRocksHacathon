import { Footer } from './components/Footer/Footer';
import { Header } from './components/Header/Header';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import { UserAuthorization } from './components/UserAuthorization/UserAuthorization';
import { MainPage } from './components/Pages/MainPage/MainPage';
import { UserRegistration } from './components/UserRegistration/UserRegistration';
import { ListPerfomance } from './components/Pages/ListPerfomance/ListPerfomance';

function App() {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path='/' element={<MainPage />}></Route>
        <Route path='/auth' element={<UserAuthorization/>}></Route>
        <Route path='/reg' element={<UserRegistration/>}></Route>
        <Route path='/listperfomance' element={<ListPerfomance/>}></Route>
      </Routes>
      <Footer />
    </BrowserRouter>
  );
}

export default App;
