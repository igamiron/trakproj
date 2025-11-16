#version 330

in vec3 in_position;
in vec3 in_normal;

uniform mat4 m_model;
uniform mat4 m_view;
uniform mat4 m_proj;

out vec3 v_normal;

void main() {
    v_normal = in_normal;
    gl_Position = m_proj * m_view * m_model * vec4(in_position, 1.0);
}
