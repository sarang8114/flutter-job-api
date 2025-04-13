from flask import Flask, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    now = datetime.utcnow()
    jobs = [
        {
            'jobId': 'api-001',
            'post': 'Software Engineer',
            'companyName': 'Google',
            'location': 'Bangalore',
            'salary': '20 LPA',
            'skills': 'Python, Cloud, DSA',
            'createdAt': (now - timedelta(days=1)).isoformat()
        },
        {
            'jobId': 'api-002',
            'post': 'Backend Developer',
            'companyName': 'Amazon',
            'location': 'Hyderabad',
            'salary': '18 LPA',
            'skills': 'Node.js, MongoDB, AWS',
            'createdAt': (now - timedelta(days=2)).isoformat()
        },
        {
            'jobId': 'api-003',
            'post': 'Android Developer',
            'companyName': 'Flipkart',
            'location': 'Bangalore',
            'salary': '12 LPA',
            'skills': 'Kotlin, Android Studio, Firebase',
            'createdAt': (now - timedelta(days=3)).isoformat()
        },
        {
            'jobId': 'api-004',
            'post': 'Frontend Engineer',
            'companyName': 'Swiggy',
            'location': 'Remote',
            'salary': '10 LPA',
            'skills': 'React, HTML, CSS',
            'createdAt': (now - timedelta(days=4)).isoformat()
        },
        {
            'jobId': 'api-005',
            'post': 'Full Stack Developer',
            'companyName': 'Zomato',
            'location': 'Gurgaon',
            'salary': '15 LPA',
            'skills': 'MERN Stack, REST APIs',
            'createdAt': (now - timedelta(days=5)).isoformat()
        },
        {
            'jobId': 'api-006',
            'post': 'Flutter Developer',
            'companyName': 'Tata Consultancy Services',
            'location': 'Pune',
            'salary': '9 LPA',
            'skills': 'Flutter, Dart, Firebase',
            'createdAt': (now - timedelta(days=6)).isoformat()
        },
        {
            'jobId': 'api-007',
            'post': 'DevOps Engineer',
            'companyName': 'Infosys',
            'location': 'Mysore',
            'salary': '13 LPA',
            'skills': 'Docker, Jenkins, Kubernetes',
            'createdAt': (now - timedelta(days=7)).isoformat()
        },
        {
            'jobId': 'api-008',
            'post': 'Data Scientist',
            'companyName': 'IBM',
            'location': 'Bangalore',
            'salary': '22 LPA',
            'skills': 'Python, ML, Pandas',
            'createdAt': (now - timedelta(days=8)).isoformat()
        },
        {
            'jobId': 'api-009',
            'post': 'UI/UX Designer',
            'companyName': 'Adobe',
            'location': 'Noida',
            'salary': '11 LPA',
            'skills': 'Figma, Adobe XD, Prototyping',
            'createdAt': (now - timedelta(days=9)).isoformat()
        },
        {
            'jobId': 'api-010',
            'post': 'Cloud Architect',
            'companyName': 'Microsoft',
            'location': 'Hyderabad',
            'salary': '28 LPA',
            'skills': 'Azure, Cloud Security',
            'createdAt': (now - timedelta(days=10)).isoformat()
        },
        {
            'jobId': 'api-011',
            'post': 'Product Manager',
            'companyName': 'Paytm',
            'location': 'Noida',
            'salary': '18 LPA',
            'skills': 'Product Lifecycle, Agile, Business Strategy',
            'createdAt': (now - timedelta(days=11)).isoformat()
        },
        {
            'jobId': 'api-012',
            'post': 'QA Engineer',
            'companyName': 'Zoho',
            'location': 'Chennai',
            'salary': '8 LPA',
            'skills': 'Automation, Selenium, JIRA',
            'createdAt': (now - timedelta(days=12)).isoformat()
        },
        {
            'jobId': 'api-013',
            'post': 'System Administrator',
            'companyName': 'HCL Technologies',
            'location': 'Lucknow',
            'salary': '7.5 LPA',
            'skills': 'Linux, Shell Scripting, Networking',
            'createdAt': (now - timedelta(days=13)).isoformat()
        },
        {
            'jobId': 'api-014',
            'post': 'Business Analyst',
            'companyName': 'Deloitte',
            'location': 'Mumbai',
            'salary': '14 LPA',
            'skills': 'Excel, SQL, Communication',
            'createdAt': (now - timedelta(days=14)).isoformat()
        },
        {
            'jobId': 'api-015',
            'post': 'Cybersecurity Analyst',
            'companyName': 'Wipro',
            'location': 'Pune',
            'salary': '16 LPA',
            'skills': 'SIEM, Threat Hunting, Firewalls',
            'createdAt': (now - timedelta(days=15)).isoformat()
        }
    ]
    return jsonify(jobs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
