import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || '/api';

// Create axios instance with auth interceptor
const apiClient = axios.create({
  baseURL: API_BASE_URL,
});

// Add JWT token to all requests
apiClient.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export interface LearningModule {
  id: number;
  name: string;
  description: string;
  type: string;
  orderIndex: number;
  topicCount?: number;
}

export interface Topic {
  id: number;
  title: string;
  description: string;
  content?: string;
  difficulty: 'BEGINNER' | 'INTERMEDIATE' | 'ADVANCED';
  orderIndex: number;
  estimatedMinutes: number;
  moduleId: number;
  moduleName?: string;
  questionCount?: number;
  codeExampleCount?: number;
}

export interface PaginatedResponse<T> {
  content: T[];
  totalElements: number;
  totalPages: number;
  size: number;
  number: number;
}

const learningService = {
  // Module operations
  getAllModules: async (): Promise<LearningModule[]> => {
    const response = await apiClient.get('/learning/modules');
    return response.data;
  },

  getModuleById: async (id: number): Promise<LearningModule> => {
    const response = await apiClient.get(`/learning/modules/${id}`);
    return response.data;
  },

  // Topic operations
  getTopicsByModule: async (
    moduleId: number,
    page: number = 0,
    size: number = 20,
    sortBy: string = 'orderIndex',
    sortDir: string = 'ASC'
  ): Promise<PaginatedResponse<Topic>> => {
    const response = await apiClient.get(
      `/learning/modules/${moduleId}/topics`,
      {
        params: { page, size, sortBy, sortDir }
      }
    );
    return response.data;
  },

  searchTopics: async (
    moduleId: number,
    searchTerm: string,
    page: number = 0,
    size: number = 20
  ): Promise<PaginatedResponse<Topic>> => {
    const response = await apiClient.get(
      `/learning/modules/${moduleId}/topics/search`,
      {
        params: { q: searchTerm, page, size }
      }
    );
    return response.data;
  },

  getTopicById: async (id: number): Promise<Topic> => {
    const response = await apiClient.get(`/learning/topics/${id}`);
    return response.data;
  },
};

export default learningService;
