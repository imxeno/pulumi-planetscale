// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.ComponentModel;
using Pulumi;

namespace Pulumi.Planetscale.Region
{
    [EnumType]
    public readonly struct Region : IEquatable<Region>
    {
        private readonly string _value;

        private Region(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static Region Here { get; } = new Region("HERE");
        public static Region OverThere { get; } = new Region("OVER_THERE");

        public static bool operator ==(Region left, Region right) => left.Equals(right);
        public static bool operator !=(Region left, Region right) => !left.Equals(right);

        public static explicit operator string(Region value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is Region other && Equals(other);
        public bool Equals(Region other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }
}
