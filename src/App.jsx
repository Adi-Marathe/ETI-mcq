import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import SubjectSelection from './components/SubjectSelection';
import UnitSelection from './components/UnitSelection';
import Quiz from './components/Quiz';
import { FiSun, FiMoon } from 'react-icons/fi';
import './index.css';

function App() {
  const [darkMode, setDarkMode] = useState(() => {
    const savedTheme = localStorage.getItem('theme');
    return savedTheme === 'dark';
  });

  useEffect(() => {
    if (darkMode) {
      document.body.classList.add('dark-mode');
      localStorage.setItem('theme', 'dark');
    } else {
      document.body.classList.remove('dark-mode');
      localStorage.setItem('theme', 'light');
    }
  }, [darkMode]);

  return (
    <Router>
      <div className={`app-container ${darkMode ? 'dark' : 'light'}`}>
        <header className="app-header">
          <Link to="/" style={{ textDecoration: 'none' }}>
            <h1>MCQ Hub</h1>
          </Link>
          <button className="theme-toggle" onClick={() => setDarkMode(!darkMode)}>
            {darkMode ? <><FiSun className="icon" /> Light Mode</> : <><FiMoon className="icon" /> Dark Mode</>}
          </button>
        </header>

        <main className="app-content">
          <Routes>
            <Route path="/" element={<SubjectSelection />} />
            <Route path="/:subjectId" element={<UnitSelection />} />
            <Route path="/:subjectId/Unit/:unitId" element={<Quiz />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
