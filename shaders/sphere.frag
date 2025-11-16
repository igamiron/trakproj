#version 330

in vec3 v_normal;
out vec4 f_color;

void main() {
    // proste światło: jaśniej gdy normalna skierowana do góry
    float l = max(dot(normalize(v_normal), normalize(vec3(0.3, 0.7, 0.5))), 0.0);
    vec3 base = vec3(0.1, 0.4, 0.9);   // niebieski
    f_color = vec4(base * (0.2 + 0.8 * l), 1.0);
}
