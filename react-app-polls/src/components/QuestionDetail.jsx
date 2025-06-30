import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import api from '../api/api';

const QuestionDetail = () => {
  const { id } = useParams();
  const [question, setQuestion] = useState(null);
  const [selectedChoice, setSelectedChoice] = useState(null);

  useEffect(() => {
    api.get(`/questions/${id}/`)
      .then((res) => setQuestion(res.data))
      .catch((err) => console.error(err));
  }, [id]);

  const vote = () => {
    api.post(`/questions/${id}/vote/`, { choice_id: selectedChoice })
      .then(() => alert("Vote submitted!"))
      .catch((err) => console.error(err));
  };

  if (!question) return <div>Loading...</div>;

  return (
    <div style={{ padding: '20px' }}>
      <h2>{question.question_text}</h2>
      {question.choices.map((choice) => (
        <div key={choice.id}>
          <label>
            <input
              type="radio"
              name="choice"
              value={choice.id}
              onChange={() => setSelectedChoice(choice.id)}
            />
            {choice.choice_text} ({choice.votes} votes)
          </label>
        </div>
      ))}
      <button onClick={vote}>Vote</button>
    </div>
  );
};

export default QuestionDetail;
