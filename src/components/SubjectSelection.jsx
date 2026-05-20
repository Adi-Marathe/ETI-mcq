import React from 'react';
import { Link } from 'react-router-dom';
import { FiBook, FiCpu, FiBriefcase } from 'react-icons/fi';

const subjects = [
  { 
    id: 'eti', 
    title: 'ETI', 
    fullName: 'Emerging Trends in Information Technology',
    description: 'AI, IoT, Blockchain, Immersive Tech, Digital Forensics',
    icon: <FiCpu />
  },
  { 
    id: 'ete', 
    title: 'ETE', 
    fullName: 'Emerging Trends in Electronics',
    description: 'Electronic trends, sensors, and modern circuits',
    icon: <FiBook />
  },
  {
    id: 'management',
    title: 'Management',
    fullName: 'Management Principles and Applications',
    description: 'Evolution of management, self-management, team dynamics',
    icon: <FiBriefcase />
  }
];

function SubjectSelection() {
  return (
    <div className="subject-selection fade-in">
      <div className="hero-section">
        <h2>Welcome to MCQ Hub</h2>
        <p>Select your subject to begin the learning journey</p>
      </div>
      
      <div className="subjects-grid">
        {subjects.map((subject) => (
          <Link 
            key={subject.id} 
            className="subject-card"
            to={`/${subject.id}`}
            style={{ textDecoration: 'none', color: 'inherit' }}
          >
            <div className="subject-icon">
              {subject.icon}
            </div>
            <div className="subject-info">
              <h3>{subject.title}</h3>
              <p className="full-name">{subject.fullName}</p>
              <p className="description">{subject.description}</p>
            </div>
            <div className="card-overlay">
              <button>View Units</button>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}

export default SubjectSelection;
