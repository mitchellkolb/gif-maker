use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

/// Adds two numbers together.
#[pyfunction]
fn add_numbers(a: i32, b: i32) -> PyResult<i32> {
    Ok(a + b)
}

/// Generates a GIF message (mock function for testing).
#[pyfunction]
fn generate_gif_message() -> PyResult<String> {
    Ok("GIF generated successfully!".to_string())
}

/// Python module definition
#[pymodule]
fn gifski_pyqt(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(add_numbers, m)?)?;
    m.add_function(wrap_pyfunction!(generate_gif_message, m)?)?;
    Ok(())
}
