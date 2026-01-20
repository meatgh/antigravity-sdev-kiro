import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || '/api';

export interface UserProgress {
  id: number;
  moduleId: number;
  moduleName: string;
  totalTopics: number;
  completedTopics: number;
  totalQuestions: number;
  completedQuestions: number;
  completionPercentage: number;
  lastAccessedAt: string;
  startedAt: string;
  completedAt?: string;
  isCompleted: boolean;
}

export interface TopicProgress {
  id: number;
  topicId: number;
  topicTitle: string;
  isCompleted: boolean;
  completionPercentage: number;
  timeSpentMinutes: number;
  questionsAttempted: number;
  questionsCorrect: number;
  accuracyPercentage: number;
  lastAccessedAt: string;
  startedAt: string;
  completedAt?: string;
  notes?: string;
}

class ProgressService {
  private getAuthHeader() {
    const token = localStorage.getItem('token');
    return token ? { Authorization: `Bearer ${token}` } : {};
  }

  async getModuleProgress(moduleId: number): Promise<UserProgress> {
    const response = await axios.get(
      `${API_BASE_URL}/progress/modules/${moduleId}`,
      { headers: this.getAuthHeader() }
    );
    return response.data;
  }

  async getAllProgress(): Promise<UserProgress[]> {
    const response = await axios.get(
      `${API_BASE_URL}/progress/modules`,
      { headers: this.getAuthHeader() }
    );
    return response.data;
  }

  async getTopicProgress(topicId: number): Promise<TopicProgress> {
    const response = await axios.get(
      `${API_BASE_URL}/progress/topics/${topicId}`,
      { headers: this.getAuthHeader() }
    );
    return response.data;
  }

  async getModuleTopicsProgress(moduleId: number): Promise<TopicProgress[]> {
    const response = await axios.get(
      `${API_BASE_URL}/progress/modules/${moduleId}/topics`,
      { headers: this.getAuthHeader() }
    );
    return response.data;
  }

  async startTopic(topicId: number): Promise<TopicProgress> {
    const response = await axios.post(
      `${API_BASE_URL}/progress/topics/${topicId}/start`,
      {},
      { headers: this.getAuthHeader() }
    );
    return response.data;
  }

  async completeTopic(topicId: number): Promise<TopicProgress> {
    const response = await axios.post(
      `${API_BASE_URL}/progress/topics/${topicId}/complete`,
      {},
      { headers: this.getAuthHeader() }
    );
    return response.data;
  }

  async updateProgress(topicId: number, percentage: number): Promise<TopicProgress> {
    const response = await axios.put(
      `${API_BASE_URL}/progress/topics/${topicId}/progress?percentage=${percentage}`,
      {},
      { headers: this.getAuthHeader() }
    );
    return response.data;
  }

  async updateTimeSpent(topicId: number, minutes: number): Promise<TopicProgress> {
    const response = await axios.put(
      `${API_BASE_URL}/progress/topics/${topicId}/time?minutes=${minutes}`,
      {},
      { headers: this.getAuthHeader() }
    );
    return response.data;
  }

  async updateQuestionStats(
    topicId: number,
    attempted: number,
    correct: number
  ): Promise<TopicProgress> {
    const response = await axios.put(
      `${API_BASE_URL}/progress/topics/${topicId}/questions?attempted=${attempted}&correct=${correct}`,
      {},
      { headers: this.getAuthHeader() }
    );
    return response.data;
  }
}

export default new ProgressService();
