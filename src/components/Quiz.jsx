import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import questionsUnit1 from '../data/questions.json';
import questionsUnit2 from '../data/unit2_questions.json';
import questionsUnit3 from '../data/unit3_questions.json';
import questionsUnit4 from '../data/unit4_questions.json';
import questionsUnit5 from '../data/unit5_questions.json';
import eteUnit1 from '../data/ete_unit1.json';
import eteUnit2 from '../data/ete_unit2.json';
import eteUnit3 from '../data/ete_unit3.json';
import eteUnit4 from '../data/ete_unit4.json';
import eteUnit5 from '../data/ete_unit5.json';
import confetti from 'canvas-confetti';
import { FiTarget, FiStar, FiCheckCircle, FiXCircle, FiAward, FiArrowLeft, FiArrowRight, FiRefreshCw } from 'react-icons/fi';

const etiUnitDataMap = {
  1: questionsUnit1,
  2: questionsUnit2,
  3: questionsUnit3,
  4: questionsUnit4,
  5: questionsUnit5,
};

const eteUnitDataMap = {
  1: eteUnit1,
  2: eteUnit2,
  3: eteUnit3,
  4: eteUnit4,
  5: eteUnit5,
};

function Quiz() {
  const { subjectId, unitId: unitIdParam } = useParams();
  const navigate = useNavigate();
  const unitId = parseInt(unitIdParam, 10);
  const storageKey = `quiz_progress_${subjectId}_unit_${unitId}`;

  const [questions, setQuestions] = useState([]);
  
  // Initialize state from localStorage if available
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(() => {
    const saved = localStorage.getItem(storageKey);
    try {
      return saved ? JSON.parse(saved).currentQuestionIndex || 0 : 0;
    } catch {
      return 0;
    }
  });
  const [answers, setAnswers] = useState(() => {
    const saved = localStorage.getItem(storageKey);
    try {
      return saved ? JSON.parse(saved).answers || {} : {};
    } catch {
      return {};
    }
  });
  const [showResults, setShowResults] = useState(() => {
    const saved = localStorage.getItem(storageKey);
    try {
      return saved ? JSON.parse(saved).showResults || false : false;
    } catch {
      return false;
    }
  });
  
  const [currentSelection, setCurrentSelection] = useState(null);
  const [isAnimating, setIsAnimating] = useState(false);

  // Save progress to localStorage whenever state changes
  useEffect(() => {
    if (questions.length > 0) {
      localStorage.setItem(storageKey, JSON.stringify({
        currentQuestionIndex,
        answers,
        showResults
      }));
    }
  }, [currentQuestionIndex, answers, showResults, storageKey, questions]);

  const onBack = () => {
    navigate(`/${subjectId}`);
  };

  const handleReset = () => {
    if (window.confirm("Are you sure you want to reset your progress for this unit?")) {
      setCurrentQuestionIndex(0);
      setAnswers({});
      setShowResults(false);
      setCurrentSelection(null);
      localStorage.removeItem(storageKey);
    }
  };

  useEffect(() => {
    const subject = subjectId?.toLowerCase();
    if (subject === 'eti') {
      const data = etiUnitDataMap[unitId];
      if (data) {
        setQuestions(data);
      } else {
        setQuestions([
          { id: 1, question: `Sample question for ETI Unit ${unitId}. Actual questions will be added later.`, options: ['a) Option A', 'b) Option B', 'c) Option C', 'd) Option D'], answer: 'a) Option A', explanation: 'This is the sample explanation.' }
        ]);
      }
    } else if (subject === 'ete') {
      const data = eteUnitDataMap[unitId];
      if (data) {
        setQuestions(data);
      } else {
        setQuestions([
          { id: 1, question: `Welcome to ETE Unit ${unitId}. Questions for this unit are being prepared.`, options: ['a) Understood', 'b) Ready', 'c) Cool', 'd) Awesome'], answer: 'a) Understood', explanation: 'This is a placeholder for ETE content.' }
        ]);
      }
    }
  }, [unitId, subjectId]);

  const handleOptionClick = (option) => {
    if (answers[currentQuestionIndex]) return;
    setCurrentSelection(option);
  };

  const handleSubmit = () => {
    if (!currentSelection) return;
    
    const currentQ = questions[currentQuestionIndex];
    const isCorrect = currentSelection.charAt(0).toLowerCase() === currentQ.answer.charAt(0).toLowerCase();
    
    if (isCorrect) {
      confetti({
        particleCount: 150,
        spread: 80,
        origin: { y: 0.6 },
        colors: ['#05cd99', '#4318ff', '#39b8ff']
      });
    }

    setAnswers(prev => ({
      ...prev,
      [currentQuestionIndex]: currentSelection
    }));
    setCurrentSelection(null);
  };

  const handleNext = () => {
    setIsAnimating(true);
    setTimeout(() => {
      const nextQuestion = currentQuestionIndex + 1;
      if (nextQuestion < questions.length) {
        setCurrentQuestionIndex(nextQuestion);
        setIsAnimating(false);
      } else {
        setShowResults(true);
      }
    }, 300);
  };

  const handlePrevious = () => {
    if (currentQuestionIndex > 0) {
      setIsAnimating(true);
      setTimeout(() => {
        setCurrentQuestionIndex(currentQuestionIndex - 1);
        setIsAnimating(false);
      }, 300);
    }
  };

  if (questions.length === 0) return <div className="loader">Loading...</div>;

  const syllabusUnits = [
    { title: 'AI & ML in Digital Security', keywords: ['security', 'attack', 'mfa', 'poisoning', 'adversarial', 'authentication', 'password', 'cybersecurity'] },
    { title: 'Generative AI', keywords: ['generative ai', 'gan', 'gpt', 'transformer', 'attention', 'text generation', 'image generation', 'foundation model', 'chatgpt'] },
    { title: 'Machine Learning & DL', keywords: ['machine learning', 'supervised', 'unsupervised', 'reinforcement', 'deep learning', 'neural network', 'backpropagation', 'data science', 'q-learning', 'k-means', 'fraud', 'pca', 'logistic regression', 'decision tree', 'overfitting', 'hidden layer', 'ml', 'dl'] },
    { title: 'Introduction of AI', keywords: ['artificial intelligence', 'ai', 'turing', 'mccarthy', 'mimic', 'types', 'narrow', 'general', 'super', 'reactive', 'theory of mind', 'healthcare', 'robotics', 'vision', 'nlp', 'natural language'] },
    { title: '5G Technology', keywords: ['5g', 'latency', 'gbps', 'network slicing', 'mmtc', 'urllc', 'beamforming'] },
    { title: 'IoT Fundamentals', keywords: ['iot', 'internet of things', 'automation', 'interconnectivity', 'interoperability', 'cloud computing', 'fog computing'] },
    { title: 'IoT Architecture & Design', keywords: ['architecture', 'perception', 'network', 'application', 'middleware', 'physical design', 'logical design', 'functional block', 'protocol', 'mqtt'] },
    { title: 'Sensors & Actuators', keywords: ['sensor', 'actuator', 'motor', 'relay', 'ldr', 'dht11', 'mq-2', 'ultrasonic', 'load cell', 'rfid'] },
    { title: 'Blockchain Basics', keywords: ['blockchain', 'decentralized', 'ledger', 'node', 'genesis block', 'immutability', 'distributed', 'satoshi', 'nakamoto', 'peer-to-peer', 'p2p', 'public', 'private', 'hybrid', 'consortium'] },
    { title: 'Consensus & Cryptography', keywords: ['consensus', 'pow', 'proof of work', 'proof of stake', 'hash', 'cryptographic', 'miner', 'mining', '51%', 'signature', 'encryption'] },
    { title: 'Smart Contracts & Applications', keywords: ['smart contract', 'ethereum', 'bitcoin', 'cryptocurrency', 'tokenization', 'nft', 'finance', 'supply chain', 'ripple', 'gas'] },
    { title: 'Immersive Technology', keywords: ['immersive', 'vr', 'ar', 'mr', 'xr', 'virtual reality', 'augmented reality', 'mixed reality', 'haptic', 'metaverse', 'headset', 'simulation'] },
    { title: 'Green Computing', keywords: ['green', 'sustainability', 'e-waste', 'virtualization', 'carbon', 'eco-friendly', 'energy', 'recycling', 'cooling'] },
    { title: 'Quantum Computing', keywords: ['quantum', 'qubit', 'superposition', 'entanglement', 'shor', 'grover', 'parallel processing'] },
    { title: 'Digital Forensics', keywords: ['forensics', 'evidence', 'chain of custody', 'volatile', 'dfrws', 'idip', 'investigation', 'hash', 'imaging', 'seizure'] },
    { title: 'Cyber Laws & Acts', keywords: ['law', 'act', 'section', 'dpdp', 'cert-in', 'it act', 'ncsp', 'cyber terrorism', 'cybercrime', 'penalty', 'data principal', 'fiduciary'] },
    { title: 'Ethical Hacking & Threats', keywords: ['hacking', 'hacker', 'phishing', 'ransomware', 'zero-day', 'deepfake', 'reconnaissance', 'exploitation', 'malware', 'ddos', 'botnet', 'vulnerability'] }
  ];

  const getTopicForQuestion = (text) => {
    const lowerText = text.toLowerCase();
    for (const unit of syllabusUnits) {
      if (unit.keywords.some(kw => lowerText.includes(kw))) {
        return unit.title;
      }
    }
    
    if (unitId === 5) return 'Digital Forensics';
    if (unitId === 4) return 'Immersive Technology';
    if (unitId === 3) return 'Blockchain Basics';
    if (unitId === 2) return 'IoT Fundamentals';
    return 'Introduction of AI';
  };

  if (showResults) {
    let correctCount = 0;
    const analytics = {};

    questions.forEach((q, index) => {
      const topic = getTopicForQuestion(q.question);
      if (!analytics[topic]) analytics[topic] = { total: 0, correct: 0 };
      analytics[topic].total += 1;
      
      const userAnswer = answers[index];
      if (userAnswer && userAnswer.charAt(0).toLowerCase() === q.answer.charAt(0).toLowerCase()) {
        analytics[topic].correct += 1;
        correctCount += 1;
      }
    });

    const areasToImprove = Object.keys(analytics).filter(topic => {
      return analytics[topic].total > 0 && (analytics[topic].correct / analytics[topic].total) < 0.7; // < 70%
    });

    return (
      <div className="results-screen zoom-in">
        <h2>Quiz Completed!</h2>
        <div className="score-display">
          <p>You scored</p>
          <h3>{correctCount} / {questions.length}</h3>
        </div>

        <div className="analytics-section">
          <h3>Performance Analytics</h3>
          <div className="analytics-grid">
            {Object.keys(analytics).map(topic => {
              if (analytics[topic].total === 0) return null;
              const percentage = Math.round((analytics[topic].correct / analytics[topic].total) * 100);
              return (
                <div key={topic} className="analytics-card">
                  <h4>{topic}</h4>
                  <div className="mini-progress-bg">
                    <div 
                      className={`mini-progress-fill ${percentage >= 70 ? 'good' : 'bad'}`} 
                      style={{ width: `${percentage}%` }}
                    ></div>
                  </div>
                  <p>{analytics[topic].correct} / {analytics[topic].total} ({percentage}%)</p>
                </div>
              );
            })}
          </div>

          {areasToImprove.length > 0 ? (
            <div className="improvement-box">
              <h4 style={{display: 'flex', alignItems: 'center', gap: '0.5rem'}}><FiTarget /> Areas to Improve</h4>
              <ul>
                {areasToImprove.map(topic => (
                  <li key={topic}>Review concepts related to <strong>{topic}</strong>.</li>
                ))}
              </ul>
            </div>
          ) : (
            <div className="improvement-box success">
              <h4 style={{display: 'flex', alignItems: 'center', gap: '0.5rem'}}><FiStar /> Excellent Work!</h4>
              <p>You have a strong understanding of all syllabus topics.</p>
            </div>
          )}
        </div>

        <button className="primary-btn mt-4" onClick={onBack}>Back to Units</button>
      </div>
    );
  }

  const currentQ = questions[currentQuestionIndex];
  const isCorrectAnswer = (opt) => opt.charAt(0).toLowerCase() === currentQ.answer.charAt(0).toLowerCase();
  
  const hasAnswered = !!answers[currentQuestionIndex];
  const submittedAnswer = answers[currentQuestionIndex];
  const activeSelection = hasAnswered ? submittedAnswer : currentSelection;

  const currentCorrectCount = Object.keys(answers).filter(index => answers[index].charAt(0).toLowerCase() === questions[index].answer.charAt(0).toLowerCase()).length;
  const currentWrongCount = Object.keys(answers).length - currentCorrectCount;

  return (
    <div className={`quiz-container ${isAnimating ? 'fade-out' : 'fade-in'}`}>
      <div className="quiz-header">
        <div className="header-actions">
          <button className="back-btn" onClick={onBack} style={{display: 'flex', alignItems: 'center', gap: '0.5rem'}}>
            <FiArrowLeft /> Exit Quiz
          </button>
          <button className="reset-btn" onClick={handleReset} style={{display: 'flex', alignItems: 'center', gap: '0.5rem'}} title="Reset Unit Progress">
            <FiRefreshCw /> Reset
          </button>
        </div>
        <div className="tracker-group">
          <div className="stats-tracker">
            <span className="stat-correct" style={{display: 'flex', alignItems: 'center', gap: '0.3rem'}}><FiCheckCircle /> {currentCorrectCount}</span>
            <span className="stat-wrong" style={{display: 'flex', alignItems: 'center', gap: '0.3rem'}}><FiXCircle /> {currentWrongCount}</span>
          </div>
          <span className="question-tracker">Question {currentQuestionIndex + 1} of {questions.length}</span>
        </div>
      </div>
      
      <div className="progress-bar-bg">
        <div 
          className="progress-bar-fill" 
          style={{ width: `${((currentQuestionIndex + 1) / questions.length) * 100}%` }}
        ></div>
      </div>

      <div className="question-box">
        <h3>{currentQ.id}. {currentQ.question}</h3>
      </div>

      <div className="options-grid">
        {currentQ.options.map((option, index) => {
          let optionClass = "option-btn";
          
          if (hasAnswered) {
            if (isCorrectAnswer(option)) {
              optionClass += " correct";
            } else if (submittedAnswer === option) {
              optionClass += " incorrect";
            }
          } else if (activeSelection === option) {
            optionClass += " selected";
          }

          return (
            <button
              key={index}
              className={optionClass}
              onClick={() => handleOptionClick(option)}
              disabled={hasAnswered}
            >
              {option}
            </button>
          );
        })}
      </div>

      {hasAnswered && (
        <div className={`explanation-box fade-in ${isCorrectAnswer(submittedAnswer) ? 'success' : 'error'}`}>
          <h4 style={{display: 'flex', alignItems: 'center', gap: '0.5rem'}}>
            {isCorrectAnswer(submittedAnswer) ? <><FiAward /> Correct!</> : <><FiXCircle /> Incorrect</>}
          </h4>
          {!isCorrectAnswer(submittedAnswer) && (
            <p className="correct-answer-text"><strong>Correct Answer:</strong> {currentQ.answer}</p>
          )}
          <p className="explanation-text"><strong>Why?</strong> {currentQ.explanation}</p>
        </div>
      )}

      <div className="quiz-navigation">
        <button 
          className="nav-btn" 
          onClick={handlePrevious} 
          disabled={currentQuestionIndex === 0}
          style={{display: 'flex', alignItems: 'center', gap: '0.5rem'}}
        >
          <FiArrowLeft /> Previous
        </button>
        
        {!hasAnswered ? (
          <button 
            className="submit-btn" 
            onClick={handleSubmit}
            disabled={!currentSelection}
          >
            Submit Answer
          </button>
        ) : (
          <button 
            className="next-btn" 
            onClick={handleNext}
            style={{display: 'flex', alignItems: 'center', gap: '0.5rem', justifyContent: 'center'}}
          >
            {currentQuestionIndex === questions.length - 1 ? 'Finish Quiz' : <>Next Question <FiArrowRight /></>}
          </button>
        )}
      </div>
    </div>
  );
}

export default Quiz;
