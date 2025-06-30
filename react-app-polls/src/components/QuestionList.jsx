import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import api from '../api/api';

const QuestionList = () => {
  const [questions, setQuestions] = useState([]);

  useEffect(() => {
    api.get('/questions/')
      .then((res) => setQuestions(res.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div style={{ padding: '20px' }}>
      <h2>Poll Questions</h2>
      <ul>
        {questions.map((q) => (
          <li key={q.id}>
            <Link to={`/questions/${q.id}`}>{q.question_text}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default QuestionList;
