import React from 'react';
import { Link } from 'react-router-dom';

const units = [
  { id: 1, title: 'Unit 1: Introduction of AI and ML', description: 'AI Concepts, Machine Learning, Generative AI, Digital Security' },
  { id: 2, title: 'Unit 2: Internet of Things', description: '5G, IoT Architecture, Sensors, Actuators, Cloud based IoT' },
  { id: 3, title: 'Unit 3: Blockchain Technology', description: 'Architecture, Types, Smart Contracts, Cryptocurrencies' },
  { id: 4, title: 'Unit 4: Immersive Tech & Sustainable Computing', description: 'AR, VR, MR, Green Computing, Quantum Computing' },
  { id: 5, title: 'Unit 5: Digital Forensics and Ethical Hacking', description: 'Investigation Models, Ethical Hacking, Cyber Security, IT Acts' }
];

function UnitSelection() {
  return (
    <div className="unit-selection fade-in">
      <h2>Select a Unit to begin the test</h2>
      <div className="units-grid">
        {units.map((unit) => (
          <Link 
            key={unit.id} 
            className="unit-card"
            to={`/Unit/${unit.id}`}
            style={{ textDecoration: 'none', color: 'inherit' }}
          >
            <h3>{unit.title}</h3>
            <p>{unit.description}</p>
            <div className="card-overlay">
              <button>Start Quiz</button>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}

export default UnitSelection;
