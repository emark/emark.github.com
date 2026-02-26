(() => {
  'use strict'

  const updateStudyProgress = async () => {
    try {
      const response = await fetch('./assets/data/study.json')
      if (!response.ok) {
        console.warn('Failed to load study.json')
        return
      }
      const data = await response.json()
      for (const [key, course] of Object.entries(data)) {
        const percent = course.y > 0 ? Math.round(course.x * 100 / course.y) : 0
        const element = document.querySelector(`[data-course-percent="${key}"]`)
        if (element) {
          element.textContent = `${percent}%`
          element.setAttribute('aria-label', `${course.x} of ${course.y} completed (${percent}%)`)
        }
      }
    } catch (e) {
      console.warn('Failed to load study progress:', e)
    }
  }

  window.addEventListener('DOMContentLoaded', updateStudyProgress)
})()
