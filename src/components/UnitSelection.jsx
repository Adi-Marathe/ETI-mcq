import React from 'react';
import { Link, useParams } from 'react-router-dom';

const etiUnits = [
  { id: 1, title: 'Unit 1: Introduction of AI and ML', description: 'AI Concepts, Machine Learning, Generative AI, Digital Security' },
  { id: 2, title: 'Unit 2: Internet of Things', description: '5G, IoT Architecture, Sensors, Actuators, Cloud based IoT' },
  { id: 3, title: 'Unit 3: Blockchain Technology', description: 'Architecture, Types, Smart Contracts, Cryptocurrencies' },
  { id: 4, title: 'Unit 4: Immersive Tech & Sustainable Computing', description: 'AR, VR, MR, Green Computing, Quantum Computing' },
  { id: 5, title: 'Unit 5: Digital Forensics and Ethical Hacking', description: 'Investigation Models, Ethical Hacking, Cyber Security, IT Acts' }
];

const eteUnits = [
  { id: 1, title: 'Unit 1: Digitalization beyond Automation', description: 'Industrial Revolutions (1.0 - 4.0), CPS, IoT, Cloud, 5G, ML, AI, and Industry 5.0' },
  { id: 2, title: 'Unit 2: Smart Grid', description: 'Need, Evolution, Layout, Components, Micro-Grids, DERs, and SAS' },
  { id: 3, title: 'Unit 3: Smart City', description: 'Urban Mobility, EV/Metro, Smart Homes, and Renewable Energy Policies' },
  { id: 4, title: 'Unit 4: Intelligent Motor Control Centers', description: 'Conventional vs Intelligent MCC, IMCC Components, and Smart Power Management' },
  { id: 5, title: 'Unit 5: Tariff and Smart Billing', description: 'PPAs, Tariff Design, Smart Metering (AMI/AMR), and Net Metering Rules' }
];

const managementUnits = [
  { id: 1, title: 'Unit 1: Introduction to Management', description: 'Evolution of management, characteristics, scientific management, self management, team management' },
  { id: 2, title: 'Unit 2: Product, Operations & Project Management', description: 'Creativity, Agile, new product development, PERT, CPM, GANTT' },
  { id: 3, title: 'Unit 3: Management Practices', description: 'Six Sigma, TQM, 5S, Lean, ISO Standards, ERP, Customer satisfaction' },
  { id: 4, title: 'Unit 4: Marketing Management', description: 'Seven Ps, Needs and Wants, CRM, Digital Marketing, Event Management' },
  { id: 5, title: 'Unit 5: Supply Chain & HR Management', description: 'Logistics, IT in SCM, HRM principles, Recruitment, Leadership' }
];

const subjectUnits = {
  eti: etiUnits,
  ete: eteUnits,
  management: managementUnits
};

function UnitSelection() {
  const { subjectId } = useParams();
  const units = subjectUnits[subjectId?.toLowerCase()] || [];

  return (
    <div className="unit-selection fade-in">
      <div className="selection-header">
        <Link to="/" className="back-link">← Back to Subjects</Link>
        <h2>{subjectId?.toUpperCase()} - Select a Unit</h2>
      </div>
      
      <div className="units-grid">
        {units.map((unit) => (
          <Link 
            key={unit.id} 
            className="unit-card"
            to={`/${subjectId}/Unit/${unit.id}`}
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
